def odczyt():
    import serial
    import struct
    ser = serial.Serial("COM6", 256000)
    while True:
        vS = ser.read(48)
        print (struct.unpack('ffffffffffff', vS))

odczyt()