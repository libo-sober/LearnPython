import os
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()
    def run(self):
        print(os.getppid(), os.getpid(), self.a, self.b, self.c)

if __name__ == '__main__':
    print(os.getpid())
    p = MyProcess(1, 2, 3)
    p.start()
    # p.terminate() # 强制结束一个子进程

#

