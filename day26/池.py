# 什么是池
    # 要在程序开始的时候,还没提交任务先创建几个线程或则进程
    # 放在一个池子里,这就是池
# 为什么要用池
    # 如果先开好进程/线程,那么有任务之后就可以直接使用这个池中的数据了
    # 并且开好的进程或者线程会一直存在池中,可以被多个任务反复使用
    # 这样极大的减少了开启/关闭调度线程/进程的时间开销
    # 池中的线程/进程个数控制了操作系统需要调度的任务个数,控制池中的单位
    # 有利于提高操作系统的效率,减轻操作系统的负担

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import current_thread
import time
import os
# threading 模块 没有提供池
# multiprocessing 模块 仿照threading写的Pool
# concurrent.futures 模块  线程池进程池  都能够使用享是的方式开启和调用/使用
# def func(a, b):
#     print(current_thread().ident, 'start', a, b)
#     time.sleep(1)  # 一开始四个全进去,然后出来一个就进去一个
#     print(current_thread().ident, 'end')
#
#
# tp = ThreadPoolExecutor(4)
# for i in range(20):
#     tp.submit(func, i, b=i+1)  # 把任务提交给池, 传参

# 实例化  创建池
# 向池中提交任务, submit 传参数
# 进程池
def func(a, b):
    print(current_thread().ident, 'start', a, b)
    time.sleep(1)  # 一开始四个全进去,然后出来一个就进去一个
    print(current_thread().ident, 'end')
    return a*b


if __name__ == '__main__':
    pp = ProcessPoolExecutor(4)
    future_l = []
    for i in range(20):
        ret = pp.submit(func, i, b=i+1)  # 把任务提交给池, 传参
        # print(ret)  # 未来对象  先返回一个对象,其结果可能还未执行,等到用result时才会拿到结果
        # print(ret.result())
        future_l.append(ret)  # 防止发生阻塞
    for ret in future_l:
        print(ret.result())

# map
# ret = pp.map(func, range(20))
# for key in ret:
#     print(key)

# 回调函数?????????  再学

