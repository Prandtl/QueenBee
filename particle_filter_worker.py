import time
import sys
import zmq
from field_object import FieldObject

def get_field_objects():
    return [FieldObject
def consumer():
    context = zmq.Context()
    reciever = context.socket(zmq.PULL)
    reciever.connect("tcp://127.0.0.1:5560")
    pusher = context.socket(zmq.PUSH)
    pusher.connect("tcp://127.0.0.1:6001")
    while True:
        work = reciever.recv_json()
        data = work["values"]
        print(data)
consumer()
