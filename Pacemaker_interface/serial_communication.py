import serial
import serial.tools.list_ports

device_hwid = 'USB VID:PID=1366:1015 SER=000000123456 LOCATION=1-1:x.0'
for port in serial.tools.list_ports.comports():
    print(port.hwid)
    if device_hwid in port.hwid:
        device = port
        print(device)


'''
ser = serial.Serial('/dev/ttyUSB0')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port
'''