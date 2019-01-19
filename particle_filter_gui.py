import zmq
import tkinter as tk
import threading

context = zmq.Context()
sock = context.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:6002")

root = tk.Tk()
c = tk.Canvas(root, width=200, height=200)
c.pack()

while True:
    root.update_idletasks()
    root.update()
    c.delete("all")
    data = sock.recv_json()
    particles = data["particles"] 
    for p in particles:
        c.create_rectangle(p["x"], p["y"], p["x"], p["y"], outline = "red")
