# multiple  多元化的
# processing  进程
# multiprocessing  多元的处理进程的模块
# from multiprocessing import Process
# import time
# import os
# def func(name, age):
#     # print(os.getpid(), os.getppid(), name, age)  # pid process id  ppid parent process id
#     print(f'发了一封邮件给{name, age}')
#     time.sleep(1)
#     print('发送完毕')
#
# if __name__ == '__main__':
#     # 只会再主进程
#     # print('main:', os.getpid(), os.getppid())
#     # p = Process(target=func, args=('alex', 82))
#     # p.start()  # 开启了一个子进程
#     arg_lst = [('大壮', 78), ('alex', 89)]
#     p_lst = []
#     for arg in arg_lst:
#         p = Process(target=func, args=arg)
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:
#         p.join()
#     print('所有的邮件都已经发送完毕')

# 能不能给子进程传递参数   可以
# 能不能获取子进程的返回值 不能
# 能不能同时开启多个子进程 可以  开启子进程时没有等他结束，就进行下一个进程  异步非阻塞
# join的用法
# p.join()  # 阻塞p这个进程，直到p执行完毕  同步阻塞
# 多进程之间的数据是否隔离  是的
from  multiprocessing import Process
n = 0
def func():
    global n
    n += 1

if __name__ == '__main__':
    p_lst = []
    for i in range(10):
        p = Process(target=func)
        p.start()
        p_lst.append(p)
    for p in p_lst:
        p.join()
    print(n)  # 0  当前进程的n不会变 变的是子进程中的n

# 使用多进程实现一个并发的socket的server



