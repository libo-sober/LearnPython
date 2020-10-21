# 数据共享的前提下雅瑶保证数据的安全性，加上lock
from multiprocessing import Process, Manager, Lock

def change_dic(dic, lock):
    with lock:
        dic['count'] -= 1


if __name__ == '__main__':
    m = Manager()
    dic = m.dict({'count':100})
    lock = Lock()
    p_lst = []
    for i in range(50):
        p = Process(target=change_dic, args=(dic, lock))
        p.start()
        p_lst.append(p)
    for p in p_lst:
        p.join()
    print(dic)