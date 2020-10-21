# 递归锁 RLock (Recursion)
    # 在同一个线程中可以acquire多次
    # 互斥锁是一个人进去,其他人都要等待哪个人出来之后才能进去,效率高
    # 递归锁,拿一把万能钥匙,其他人在等,里边有多个门,都打开.出来后,其他人才能进去

# from threading import Lock, RLock
# rl = RLock()
# rl.acquire()
# rl.acquire()
# rl.acquire()
# rl.acquire()
# print('锁住的代码')
# rl.acquire()
# rl.acquire()
# rl.acquire()
# rl.acquire()
# l = Lock()
# l.acquire()
# print('锁住的代码')
# l.release()
# from threading import  RLock, Thread
#
# def func(i, lock):
#     lock.acquire()
#     lock.acquire()
#     lock.acquire()
#     print(f'{i}:start')
#     lock.release()
#     # lock.release()
#     # lock.release()
#     print(f'{i}:end')
# lock = RLock()
# for i in range(5):
#     Thread(target=func, args=(i, lock)).start()
# 死锁现象
# 科学家吃面  一个拿到叉子 一个拿到面 都吃不到  死锁
from threading import Lock, Thread, RLock
import time

# noodle_lock = Lock()
# fork_lock = Lock()
noodle_lock = fork_lock = RLock()  # 这样就不会死锁了

def eat(name):
    noodle_lock.acquire() # 抢到面了
    print(f'{name}抢到面了')
    fork_lock.acquire()
    print(f'{name}抢到叉子了')
    print(f'{name}吃面')
    time.sleep(0.1)
    fork_lock.release()
    print(f'{name}放下叉子了')
    noodle_lock.release()
    print(f'{name}放下面了')

def eat2(name):
    fork_lock.acquire()
    print(f'{name}抢到叉子了')
    noodle_lock.acquire()  # 抢到面了
    print(f'{name}抢到面了')
    print(f'{name}吃面')
    time.sleep(0.1)
    noodle_lock.release()
    print(f'{name}放下面了')
    fork_lock.release()
    print(f'{name}放下叉子了')


Thread(target=eat, args=('alex',)).start()
Thread(target=eat2, args=('taibai',)).start()
Thread(target=eat, args=('wusie',)).start()
Thread(target=eat2, args=('dazhuang',)).start()

# 死锁现象产生的原因:多把锁 并且在多个线程中交替使用
# 如果是互斥锁出现了死锁现象,最快速的解决方法就是把所有的互斥锁变成一把递归锁
# 如果非要用互斥锁,就改为一把锁,锁住面条和叉子



