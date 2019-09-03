from __future__ import print_function

import signal
import pyuv

def on_connection(server, error):
    client = pyuv.TCP(server.loop)
    # client.keepalive(False, 0)
    server.accept(client)
    clients.append(client)
    # with open("500b.html", "rb") as file:
    #     client.write(file.read())
    client.write("Yeet\n".encode('ascii'))
    client.shutdown()
    # client.close()

def signal_cb(handle, signum):
    [c.close() for c in clients]
    signal_h.close()
    server.shutdown()
    server.close()


print("PyUV version %s" % pyuv.__version__)

loop = pyuv.Loop.default_loop()
clients = []

server = pyuv.TCP(loop)
server.bind(("0.0.0.0", 1234))
server.listen(on_connection)

signal_h = pyuv.Signal(loop)
signal_h.start(signal_cb, signal.SIGINT)

loop.run()
print("Stopped!")
