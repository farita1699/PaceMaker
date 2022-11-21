import serial
import serial.tools.list_ports
import io

#Another way of finding the port
'''
device_hwid = 'USB VID:PID=1366:1015 SER=000000123456 LOCATION=1-1:x.0'
for port in serial.tools.list_ports.comports():
    print(port.hwid)
    if device_hwid in port.hwid:
        device = port
        print(device)
'''

ser = serial.Serial('COM3')  # open serial port on Windows
ser.baudrate = 115200  #Baudrate as provided in tutorial file
print(ser.name)         # check which port was really used

