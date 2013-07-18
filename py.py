#sub
import zmq
import re
import time

ipc_r_to_py = "ipc:///tmp/r_to_py.sock"
ipc_py_to_r = "ipc:///tmp/py_to_r.sock"
tcp_r_to_py = "tcp://127.0.0.1:5000"
tcp_py_to_r = "tcp://127.0.0.1:6000"

context = zmq.Context()
sub_socket = context.socket(zmq.SUB)
sub_socket.connect(tcp_r_to_py)
sub_socket.setsockopt(zmq.SUBSCRIBE, "r")
 
pub_socket = context.socket(zmq.PUB)
pub_socket.bind("ipc:///tmp/py_to_r.sock")

#time.sleep(1)


while True:
#    print sub_socket.recv()
    msg_raw = sub_socket.recv()
    msg = re.sub(r'^r ', "", msg_raw)
    print "got msg: %s" % msg
    result = eval(msg)
    pub_socket.send(str(result))
