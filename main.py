import serial

def make_important_stuff():
    for i in range(0,1000000):
        if i % 100000 == 0:
            print(i)

with serial.Serial('/dev/ttyUSB0', 19200, timeout=1) as ser:
    while True:
        ser.reset_input_buffer()
        line = ser.readline()
        print(line)
        make_important_stuff()
        print('-------------')

