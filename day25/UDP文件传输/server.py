import socket

sk = socket.socket(type=socket.SOCK_DGRAM)  # UDP 协议
sk.bind(('127.0.0.1', 9000))

msg, addr = sk.recvfrom(1024)
print(msg)
sk.sendto(b'recv', addr)



