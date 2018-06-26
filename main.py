import serial

def parse(raw):
    stripped = raw.strip()
    values = stripped.split(',')
    print(len(values))
    if len(values) != 3:
        raise Exception('wrong amount of values')
    return values

def make_particle_filter_step(data):
    for i in data:
        print(i)
    print('---------------')

with serial.Serial('/dev/ttyUSB0', 19200, timeout=1) as ser:
    while True:
        ser.reset_input_buffer()
        ser.readline()
        line = ser.readline().decode("utf-8")
        try:
            data = parse(line)
            make_particle_filter_step(data)
        except:
            print('[D]caught')

