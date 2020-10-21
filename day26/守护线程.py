# import time
# from threading import Thread
#
# def son():
#     while True:
#         print('in son')
#         time.sleep(1)
# def son2():
#     for i in range(10):
#         print('in son2')
#         time.sleep(1)
# t = Thread(target=son)
# t.daemon = True  # 守护线程，子线程随着主线程结束而结束
# Thread(target=son2).start()  # 守护线程会再主线程的代码结束之后继续守护其他子线程
# t.start()
# 主线程会等待子线程结束后才结束
# 为什么？
    # 主线程结束进程就会结束
# 守护线程会再主线程的代码结束之后继续守护其他子线程
# 为什么？
    # 守护线程随着进程的结束才结束

# 线程锁
from threading import Thread,Lock
n = 0
def add(lock):
    with lock:
        for i in range(200000):
            global n
            n += 1

def sub(lock):
    with lock:
        for i in range(200000):
            global n
            n -= 1
lock = Lock()
Thread(target=add, args=(lock,))
Thread(target=sub, args=(lock,))
print(n)

# += -= 数据不安全  因为 + 和 赋值是分开的操作
# append pop 就安全
# 解决线程数据不安全的问题加锁


