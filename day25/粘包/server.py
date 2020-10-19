import struct
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

conn, addr = sk.accept()
msg1 = input('...').encode('utf-8')
msg2 = input('...').encode('utf-8')
blen1 = struct.pack('i', len(msg1))
conn.send(blen1)
conn.send(msg1)
blen2 = struct.pack('i', len(msg2))
conn.send(blen2)
conn.send(msg2)

sk.close()
# encode()  decode()  用什么方式编码 就用什么方式解码

# 基于TCP协议的文件传输

