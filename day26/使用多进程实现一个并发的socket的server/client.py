import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

while True:
    sk.send(b'hello')
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    time.sleep(0.5)

sk.close()
