import socket
import struct
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

time.sleep(0.1)
blen1 = sk.recv(4)
blen1 = struct.unpack('i', blen1)
msg1 = sk.recv(blen1[0])
print(msg1.decode('utf-8'))
blen2 = sk.recv(4)
blen2 = struct.unpack('i', blen2)
msg2 = sk.recv(blen2[0])
print(msg2.decode('utf-8'))

sk.close()
