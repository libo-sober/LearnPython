# 网络开发架构
#     C/S架构 : 需要安装一下才能使用
#         CLIENT
#         SERVER
#         可以离线使用/更安全
#     B/S架构
#         browser
#         server
#         不需要安装也能使用
#     B/S也是C/S的一种
#     统一用户的入口
#
import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()
while True:
    conn, addr = sk.accept()
    while True:
        send_m = input('>>>')
        conn.send(send_m.encode('utf-8'))
        if send_m.upper() == 'Q':
            break
        msg = conn.recv(1024)
        msg2 = msg.decode('utf-8')
        if msg2.upper() == 'Q':
            break
        print(msg2)
    conn.close()

sk.close()
# encode()  decode()  用什么方式编码 就用什么方式解码

# 基于TCP协议的文件传输

