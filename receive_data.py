import serial
while True:
    ser = serial.Serial("/dev/tty.HC-05-SPPDev")
    ser.flushInput()
    ser_bytes = ser.readline()
    decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    print(decoded_bytes)

