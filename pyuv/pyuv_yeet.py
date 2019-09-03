from __future__ import print_function

import signal
import pyuv
import time

server = None
signal_h = None

def main():
    global server, signal_h
    print("PyUV version %s" % pyuv.__version__)

    loop = pyuv.Loop.default_loop()
    # clients = []

    server = pyuv.TCP(loop)
    server.bind(("0.0.0.0", 1234))
    server.listen(on_connection)

    signal_h = pyuv.Signal(loop)
    signal_h.start(signal_cb, signal.SIGINT)

    loop.run()
    print("Stopped!")

def on_connection(server, error):
    client = pyuv.TCP(server.loop)
    server.accept(client)
    # clients.append(client)
    with open("test-pages/500b.html", "rb") as file:
        client.write(file.read())
    # client.write("Yeet\n".encode('ascii'))
    client.shutdown(on_shutdown)

def on_shutdown(client, err):
    client.close()

def signal_cb(handle, signum):
    global server, signal_h
    # [c.close() for c in clients]
    signal_h.close()
    server.close()

if __name__ == "__main__":
    main()