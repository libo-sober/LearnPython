# import queue  # 线程之间数据安全的容器队列
#
# q = queue.Queue(4)  # FIFO 先进先出
# # q.put(1)
# q.put(2)
# # q.get()
# q.put(3)
# q.put(4)
# print('4 done')
# q.put(5)
# print('5 done')

# q.get_nowait()
# q.put_nowait()

from queue import LifoQueue, PriorityQueue
# LifoQueue  last in first out 后进先出
# PriorityQueue 优先级队列
priq = PriorityQueue()
priq.put((2, 'alex'))
priq.put((5, 'xia'))
priq.put((0, 'ming'))

print(priq.get())
print(priq.get())
print(priq.get())
# (0, 'ming')
# (2, 'alex')
# (5, 'xia')

# 线程队列 主要记住用法
    # 先进先出 Queue
    # 后进先出 LifoQueue
    # 优先级 PriorityQueue
