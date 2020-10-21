# 互斥锁  不能载同一个进程中连续acquire多次
# 进程之间数据安全的问题
# 抢票的例子
import json
import time
from multiprocessing import Process, Lock

def search(i):
    with open('ticket', encoding='utf-8') as f:
        ticket = json.load(f)
    print(f"{i}:当前的余票是{ticket['count']}")

def buy_ticket(i):
    with open('ticket', encoding='utf-8') as f:
        ticket = json.load(f)
    if ticket['count'] > 0:
        ticket['count'] -= 1
        print(f'{i}买到票了')
    time.sleep(0.2)
    with open('ticket', mode='w', encoding='utf-8') as f:
        json.dump(ticket, f)
def get_ticket(i, lock):
    search(i)
    # lock.acquire()
    # buy_ticket(i)
    # lock.release()
    # 等同
    with lock:  # 代替上边，并能做一些异常处理，保证一个代码出错下一个进程也能执行
        buy_ticket(i)
if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        Process(target=get_ticket, args=(i, lock)).start()
# 这种只有一张票 所有人都能买
# import time
# from multiprocessing import Lock, Process
#
# def func(i, lock):
#     lock.acquire()  # 拿钥匙
#     print(f'被锁住的代码{i}')
#     time.sleep(1)
#     lock.release()  # 还钥匙
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         Process(target=func, args=(i, lock)).start()


