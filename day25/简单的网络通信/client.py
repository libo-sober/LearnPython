import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

while True:
    msg = sk.recv(1024)
    msg2 = msg.decode('utf-8')
    if msg2.upper() == 'Q':
        break
    print(msg2)
    send_m = input('>>>')
    sk.send(send_m.encode('utf-8'))
    if send_m.upper() == 'Q':
        break

sk.close()
