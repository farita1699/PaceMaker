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


class _SerialHandler(QThread):
    _running: bool
    _buf: bytearray
    _conn: Serial
    _lock: Lock

    ecg_data_update: pyqtSignal = pyqtSignal(float, float)


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
        self._sent_data = bytes()
        self._req_ecg = False
        self.atr = True
        self.vent = True
        self._lock = Lock() 

        
    def run(self):
        self._running = True

        while self._running:
            if self._conn.is_open:
                try:
                    with self._lock:
                        if self._req_ecg:
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
        if self._conn.in_waiting < 28: 
            self._req_ecg = True
            #print("Line 100: ", self._conn.in_waiting)
            return
        #print("Running")
        returned = unpack("=2d6B2H2B", self._conn.read(28))
        print("Returned: ", returned)
        atr_val = returned[0] if atr else 0
        vent_val = returned[1] if vent else 0
        if atr or vent:
            self.ecg_data_update.emit(atr_val, vent_val)
            self._req_ecg = True

    def send_params_to_pacemaker(self, params_to_send: Dict) -> None:
        with self._lock:
            self._req_ecg = True
            
            paramarray = [12, 5, *[int(params_to_send[key]) for key in self._PARAMS_ORDER]]
            #paramarray = [12, 5, 1, 3, 3, 60, 5, 5, 250, 320, 4, 4]
            print('Sending Data:')
            print(paramarray)
            self._conn.write(pack("=8B2H2B", *paramarray))
            sleep(0.1)
            self._conn.write(pack("=8B2H2B", *paramarray))
            sleep(0.1)

    def _try_to_open_port(self) -> None:
        with self._lock:
            try:
                self._conn.open()
                print("Opened Port")
            except SerialException:
                pass

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
    device_connected: pyqtSignal = pyqtSignal(bool)
    def __init__(self):
        super().__init__()

        self.ser = _SerialHandler()
        self.ser.start()
        # self.ser.start_serial_comm('COM3')
          
    def run(self):
        self._device = self._filter_devices(list_ports.comports()) 
        if (len(self._device)):
                self.ser.start_serial_comm(self._device[0].device)
                self.device_connected.emit(True)
        else:
            self.device_connected.emit(False)  

    @staticmethod
    def _filter_devices(data: List[ListPortInfo]) -> List[ListPortInfo]:
        return [dev for dev in data if dev.vid == 0x1366 and dev.pid == 0x1015]
    def send_data_to_pacemaker(self, params: Dict) -> None:
        self.ser._running = True
        self.ser.send_params_to_pacemaker(params)
    def stop(self):
        self.ser._running = False
        


