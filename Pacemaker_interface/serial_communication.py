from enum import Enum, unique
from struct import calcsize, pack, unpack, unpack_from
from threading import Lock, Timer
from time import sleep
from typing import Dict, List, Optional, Union

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from serial import Serial, SerialException
from serial.tools import list_ports
from serial.tools.list_ports_common import ListPortInfo

#Another way of finding the port
'''
device_hwid = 'USB VID:PID=1366:1015 SER=000000123456 LOCATION=1-1:x.0'
for port in serial.tools.list_ports.comports():
    print(port.hwid)
    if device_hwid in port.hwid:
        device = port
        print(device)
'''

@unique
class PacemakerState(Enum):
    NOT_CONNECTED = 1
    CONNECTED = 2
    REGISTERED = 3

class _SerialHandler(QThread):
    _running: bool
    _buf: bytearray
    _conn: Serial
    _num_bytes_to_read: int
    _sent_data: bytes
    _send_params: bool
    _lock: Lock

    ecg_data_update: pyqtSignal = pyqtSignal(float, float)

    params_received: pyqtSignal = pyqtSignal(bool, str)

    _num_floats = 20
    _PARAMS_FMT_STR, _ECG_FMT_STR, _ECG_DATA_STR = "=6BH3BHH3BHBB", f"={_num_floats}f", f"={_num_floats // 2}f"
    _PARAMS_NUM_BYTES, _ECG_NUM_BYTES, _ECG_DATA = calcsize(_PARAMS_FMT_STR), calcsize(_ECG_FMT_STR), calcsize(
        _ECG_DATA_STR)
    _PARAMS_ORDER = ["Pacing Mode", "Atrial Pulse Width", "Ventricular Pulse Width",
                    "Lower Rate Limit", "Atrial Amplitude", "Ventricular Amplitude",
                    "Atrial Refractory Period", "Ventricular Refractory Period", "Atrial Sensitivity",
                    "Ventricular Sensitivity"]

    def __init__(self):
        super().__init__()
        print("Serial handler init")

        self._running = False
        self._buf = bytearray()
        self._conn = Serial(baudrate=115200, timeout=10)
        self._num_bytes_to_read = self._ECG_NUM_BYTES + 1
        self._sent_data = bytes()
        self._send_params = False
        self._req_ecg = False
        self._req_com = True
        self.atr = True
        self.vent = True
        self._lock = Lock() 

        
    def run(self):
        self._running = True

        while self._running:
            if self._conn.is_open:
                try:
                    with self._lock:
                        if self._send_params: 
                            self._send_params = False
                            self._conn.write(self._sent_data)
                        elif self._req_ecg:
                            self._req_ecg = False
                            # ["Pacing Mode", "Atrial Pulse Width", "Ventricular Pulse Width",
                            # "Lower Rate Limit", "Atrial Amplitude", "Ventricular Amplitude",
                            # "Atrial Refractory Period", "Ventricular Refractory Period", "Atrial Sensitivity",
                            # "Ventricular Sensitivity"]
                            req_array = [12, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                            req_bytes = pack("=8B2H2B", *req_array)
                            self._conn.write(req_bytes)
                            Timer(0.02, self.read_data, args=(self.atr, self.vent)).start()
                except Exception as e:
                    print(e)
                    pass
            elif self._conn.port:
                self._try_to_open_port()
            else:
                sleep(1)

    def read_data(self, atr: bool, vent: bool) -> None:
        if self._conn.in_waiting < 16: 
            self._req_ecg = True
            #print("Line 100: ", self._conn.in_waiting)
            return
        #print("Running")
        returned = unpack("=2H6B2H2B", self._conn.read(16))
        #print("Returned: ", returned)
        atr_val = returned[0]/10000 if atr else 0
        vent_val = returned[1]/10000 if vent else 0
        if atr or vent:
            self.ecg_data_update.emit(atr_val, vent_val)
            self._req_ecg = True

    def send_params_to_pacemaker(self, params_to_send: Dict) -> None:
        with self._lock:
            self._req_com = False
            self._req_ecg = True
            paramarray = [12, 5, *[int(params_to_send[key]) for key in self._PARAMS_ORDER]]
            print('Sending Data:')
            print(paramarray)
            self._conn.write(pack("=8B2H2B", *paramarray))
            sleep(0.1)
            self._conn.write(pack("=8B2H2B", *paramarray))
            sleep(0.1)

    # Read the output stream of the pacemaker
    def _readline(self) -> bytearray:
        buf_len: int = len(self._buf)

        if buf_len >= self._num_bytes_to_read:
            r = self._buf[:self._num_bytes_to_read]
            self._buf = self._buf[self._num_bytes_to_read:]
            return r

        while self._running and self._conn.is_open:
            data: Optional[bytes] = self._conn.read(self._num_bytes_to_read)
            buf_len = len(self._buf)

            if buf_len >= self._num_bytes_to_read:
                r = self._buf[:self._num_bytes_to_read]
                self._buf = self._buf[self._num_bytes_to_read:] + data
                return r
            else:
                self._buf.extend(data)

    def _try_to_open_port(self) -> None:
        with self._lock:
            try:
                self._conn.open()
                print("Opened Port")
            except SerialException:
                pass

    def _verify_params(self, received_params: bytes) -> None:
        if self._sent_data != bytes(received_params[:self._PARAMS_NUM_BYTES]):
            self.params_received.emit(False, "The received parameters were not the same as the sent ones!\nPlease "
                                             "restart the DCM/Pacemaker or try a different Pacemaker!")
        else:
            self.params_received.emit(True, "Successfully sent parameters!")

    def stop(self) -> None:
        with self._lock:
            self._running = False
            self._conn.close()

    def start_serial_comm(self, port: str) -> None:
        print(f"Opening serial port {port} with pacemaker")
        self._buf = bytearray()
        with self._lock:
            self._conn.port = port

    def stop_serial_comm(self) -> None:
        with self._lock:
            self._conn.close()
            self._conn.port = None

class ConnectionHandler(QThread):
    def __init__(self):
        self.ser = _SerialHandler()
        self.ser.start()
        self.ser.start_serial_comm('COM3')
    def send_data_to_pacemaker(self, params: Dict) -> None:
        self.ser._running = True
        self.ser.send_params_to_pacemaker(params)
    def stop(self):
        self.ser._running = False
        


