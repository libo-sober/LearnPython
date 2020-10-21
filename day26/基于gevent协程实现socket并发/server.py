from gevent import monkey
monkey.patch_all()
import socket
import gevent
def func(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        MSG = msg.upper()
        conn.send(MSG.encode('utf-8'))


sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

while True:
    conn, _ = sk.accept()
    gevent.spawn(func, conn)
