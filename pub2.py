import zmq
from random import choice
import time
context = zmq.Context()
socket = context.socket(zmq.PUB)

ipc_r_to_py = "ipc:///tmp/r_to_py.sock"
ipc_py_to_r = "ipc:///tmp/py_to_r.sock"
tcp_r_to_py = "tcp://127.0.0.1:5000"
tcp_py_to_r = "tcp://127.0.0.1:6000"


socket.bind(tcp_r_to_py)
 
time.sleep(1)

#while True:
socket.send( "r hi")
