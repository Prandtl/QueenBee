import random
import zmq

N = 1000

def generator():
    context = zmq.Context()
    sock = context.socket(zmq.PUSH)
    sock.connect("tcp://127.0.0.1:6001")
    
    while True:
        particles = [{"x": random.randint(0, 100), "y": random.randint(0, 100)} for i in range(0, N)]
        sock.send_json({"particles": particles})
generator()
