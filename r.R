library(zmqc)

ipc_r_to_py = "ipc:///tmp/r_to_py.sock"
ipc_py_to_r = "ipc:///tmp/py_to_r.sock"
tcp_r_to_py = "tcp://127.0.0.1:5000"
tcp_py_to_r = "tcp://127.0.0.1:6000"

if (exists("pub")) try(close(pub), silent=TRUE)
if (exists("sub")) try(close(sub), silent=TRUE)

pub <- zmqc(tcp_r_to_py, "w")
sub <- zmqc(tcp_py_to_r)

Sys.sleep(1) 

writeLines("r 2 + 2", pub, sep="")
Sys.sleep(1)

readLines(sub, 1)
#fromPy <- readLines(sub, 1)

