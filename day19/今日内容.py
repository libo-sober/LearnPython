"""
模块和实际工作时间的关系

正则表达式  *****

re模块

自动化运维---开发
爬虫

"""
"""

"""
class Node:
    def __init__(self, node, length):
        self.node = node
        self.length = length

class Edge:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

def cmp(e1, e2):
    return e1.length < e2.length

class Prim:
    def __init__(self, n, m):
        self.n = n  # 输入的点个数
        self.m = m  # 输入的边个数
        self.v = []  # 存放所有节点之间的可达关系与距离
        self.e = []  # 存放与当前已选节点相连的边
        self.s = []  # 存放最小生成树里的所有边
        self.vis = set()  # 标记每个点是否被访问过

    def make(self):
        for i in range(self.m):
            x, y, length = list(map(int, input().split()))
            self.v[x].append(Node(y, length))


    def insert(self, point):
        """往Vnew中插入一个新的点"""
        for i in range(v[point].size()):
            pass


def main():
    n, m = list(map(int, input().split()))
    prim = Prim(n, m)


if __name__ == '__main__':
    main()

g = Graph()