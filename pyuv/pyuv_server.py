import signal
import pyuv
import re

server = None
sigint_watcher = None
# If we set the payload as a global variable, somehow it will be slower
# payload = "HTTP/1.1 200 OK\r\n\r\n".encode('ascii')
# with open("test-pages/20kb.html", "rb") as file:
#     payload += file.read()

def main():
    global server, sigint_watcher, file_dir
    print("Started!")

    loop = pyuv.Loop.default_loop()
    # Caching test
    # data = "HTTP/1.1 200 OK\r\n\r\n".encode('ascii')
    # with open(file_dir, "rb") as file:
    #     data += file.read()
    # loop.payload = data

    server = pyuv.TCP(loop)
    server.bind(("0.0.0.0", 1234))
    server.listen(on_connection)

    sigint_watcher = pyuv.Signal(loop)
    sigint_watcher.start(on_sigint, signal.SIGINT)

    loop.run()
    print("Stopped!")

def on_connection(server, error):
    client = pyuv.TCP(server.loop)
    # client.payload = server.loop.payload
    server.accept(client)
    client.start_read(on_read)

def on_read(client, data, error):
    if data is None:
        client.shutdown(on_shutdown)
        return

    path_match = re.search(rb"GET (.*) ", data)
    if path_match:
        path = path_match.group(1).decode("utf-8")
        print("[GET]", path)
    else:
        client.write("HTTP/1.1 400 Bad Request\r\n\r\n".encode('ascii'), on_write)
        return

    try:
        file_path = path[1:]
        with open(file_path, "rb") as file:
            client.write("HTTP/1.1 200 OK\r\n\r\n".encode('ascii') + file.read(), on_write)
    except:
        client.write("HTTP/1.1 404 Not Found\r\n\r\n".encode('ascii'), on_write)

def on_write(client, err):
    client.shutdown(on_shutdown)    

def on_shutdown(client, err):
    client.close()

def on_sigint(handle, signum):
    global server, sigint_watcher
    print("Interrupted!")
    sigint_watcher.close()
    server.close()

if __name__ == "__main__":
    main()