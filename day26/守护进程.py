from multiprocessing import Process
import time

def son1():
    while True:
        print('in son1')
        time.sleep(1)

def son2():
    for i in range(10):
        print('in son2')
        time.sleep(1)

if __name__ == '__main__':
    p1 = Process(target=son1)
    p1.daemon = True  # 表示设置p1为守护进程
    p1.start()
    p2 = Process(target=son2)
    p2.start()
    p2.join()
    time.sleep(5)
    print('in main')
    # 会输出5个 in son1

# 主进程会等待所有子进程结束， 是为了回收子进程资源
# 守护进程会等待主进程的代码执行结束之后再结束,只守护主进程的代码时间
# 主进程的代码什么时候结束，守护进程就什么时候结束，和其他子进程无关
# 要求守护进程必须在p2结束后再结束


