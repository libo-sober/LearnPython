import socket
import json
import struct

# 接收
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

conn, _ = sk.accept()
blen = conn.recv(4)
blen = struct.unpack('i', blen)
msg = conn.recv(blen[0]).decode('utf-8')
msg = json.loads(msg)
# print(msg)
with open(msg['filename'], mode='wb') as f:
    while msg['filesize'] > 0:
        content = conn.recv(1024)
        msg['filesize'] -= 1024
        f.write(content)

conn.close()
sk.close()



