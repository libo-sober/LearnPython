# 进程：数据隔离，资源分配的最小单位，可以利用多核，操作系统调度
    # 如何开启进程 multiprocessing， 如何开启 start join
    # 进程有数据不安全问题 Lock
    # 进程之间可以通信：
        # 队列(安全)  管道
        # 第三方工具：redis
    # 进程之间数据共享 Manager
    # 生产者消费者模型


# 线程
    # 什么是线程：能被操作系统调度的最小单位
    # 一个进程可以有多个线程
    # 同一个进程中多个线程同时被cpu执行？ 就是这样的
    # 可以利用多核， 数据共享，开启关闭切换时间开销小

# CPython中的多线程
    # gc 垃圾回收机制
        # 引用计数 + 分代回收
    # 全局解释器锁是未来完成gc的回收机制
    # 全局解释器锁（GIL）global interpreter lock
        # 导致了同一个进程中的多个线程只能有一个线程真正被cpu执行
    # 节省的是IO操作时间

# threading模块
import time
from  threading import Thread, current_thread, enumerate, active_count
# current_thread() 获取线程id   current_thread().ident 获取线程id
def func(i):
    print(f'start{i},{current_thread()}')
    time.sleep(1)
    print(f'end{i}')


if __name__ == '__main__':
    t1 = []
    for i in range(10):
        t = Thread(target=func, args=(i,))
        t.start()
        t1.append(t)
    print(enumerate(), active_count()) # 11个 还有一个主线程
    for t in t1:
        t.join()
    # print(enumerate(), active_count())  # 1个 只剩1个主线程
    print('所有的线程都执行完了')

# 线程是不能从外部terminate
# 所有的线程必须自己执行完毕
# enumerate 列表 存储了所有活着的线程对象
# active_count 数字 存储了所有或者的线程个数
# 面向对象的方式开启一个线程
# 线程之间的数据是共享的
