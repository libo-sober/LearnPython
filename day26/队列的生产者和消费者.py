# 进程之间数据隔离


# 进程之间通信（IPC） Inter Process Communication
    # 基于文件：同一台机器上的多个进程之间的通信 Queue
#     # 基于网络：同一台机器或者多态机器上的多进程通信
# from multiprocessing import Queue, Process
#
# def son(q):
#     q.put('hello')
#
# if __name__ == '__main__':
#     q = Queue()
#     Process(target=son, args=(q, )).start()
#     print(q.get())
#     # son 和 mian 之间的通信

# 生产者消费者模型
#   爬虫的时候
#   分布式
#   本质就是让生产数据和消费数据的效率达到平衡并且最大化的效率
# from multiprocessing import Process, Queue
# import time
# import random
#
# def consumer(q):#  消费者：通常取到数据之后还要进行某些操作
#     for i in range(10):
#         print(q.get())
#
#
# def producer(q):  # 生产者：通常再放数据前需要先通过某些代码来获取数据
#     for i in range(10):
#         time.sleep(random.random())
#         q.put(i)
#
#
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=consumer, args=(q,))
#     p1 = Process(target=producer, args=(q,))
#     c1.start()
#     p1.start()
# import requests
# from multiprocessing import Process, Queue
#
# def producer(i, url, q):
#     ret = requests.get(url)
#     q.put((i, ret.status_code))
#     # print(ret.status_code)
#
# if __name__ == '__main__':
#     q = Queue()
#     url_lst = ['https://www.cnblogs.com/Eva-J/p/7277026.html',
#                'https://blog.csdn.net/qq_31910669',
#                'https://blog.csdn.net/qq_31910669/article/details/109136837']
#     # for i, url in enumerate(url_lst):
#     #     producer(i, url, '1')
#     for index, url in enumerate(url_lst):
#         Process(target=producer, args=(index, url, q)).start()
#     for i in range(3):  # 异步阻塞， 等哪个子进程先结束我就先获取谁的结果
#         print(q.get())
import requests
from multiprocessing import Process, Queue

def producer(i, url, q):
    ret = requests.get(url)
    q.put((i, ret.text))
    # print(ret.status_code)

def consumer(q):
    while True:
        res = q.get()
        if res is None:
            break
        with open(f'{res[0]}.html', mode='w', encoding='utf-8') as f:
            f.write(res[1])


if __name__ == '__main__':
    q = Queue()
    url_dic = {'cn':'https://www.cnblogs.com/Eva-J/p/7277026.html',
               'mu':'https://blog.csdn.net/qq_31910669',
               'li':'https://blog.csdn.net/qq_31910669/article/details/109136837'}
    p = []
    for key in url_dic:
        p1 = Process(target=producer, args=(key, url_dic[key], q))
        p1.start()
        p.append(p1)
    Process(target=consumer, args=(q,)).start()
    for p2 in p:
        p2.join()
    q.put(None)
