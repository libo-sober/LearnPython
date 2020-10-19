"""
基础数据类型
流程控制：条件判断 循环
文件操作
函数
    基础
    装饰器
        带参装饰器-----
    生成器 迭代器
    递归函数----
常用模块
    random
    hashlib
    time datetime
    sys
    os
    json/pickle
    collection
    re---------
    logging------------
    包的导入-----------
面向对象--------6
网络编程---------4
并发编程--------5
数据库------------5
"""
import math
class Edge:
    """
    Edge类表示边的信息
    x,y表示这条边的两个顶点
    length为<x,y>之间的距离
    """
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

class UnionFindSet:
    """并查集类，用于连通两个节点以及判断图中的所有节点是否连通 """
    def __init__(self, start, n):
        self.start = start  # start和n分别用于指示并查集里节点的起点和终点
        self.n = n
        self.pre = [0 for i in range(self.n - self.start + 2)]  # pre数组用于存放某个节点的上级
        self.rank = [0 for i in range(self.n - self.start + 2)]  # rank数组用于降低关系树的高度

    def init(self):
        """初始化并查集"""
        for i in range(self.start, self.n+1):
            self.pre[i] = i
            self.rank[i] = 1

    def find_pre(self, x):
        """寻找节点x的上一级节点"""
        if self.pre[x] == x:
            return x
        else:
            self.pre[x] = self.find_pre(self.pre[x])
        return self.pre[x]

    def is_same(self, x, y):
        """判断x节点和y节点是否连通"""
        return self.find_pre(x) == self.find_pre(y)

    def unite(self, x, y):
        """判断两个节点是否连通，如果未连通则将其连通并返回真，否则返回假"""
        x = self.find_pre(x)
        y = self.find_pre(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:
            """类似于平衡二叉树的概念"""
            self.pre[y] = x
        else:
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.pre[x] = y
        return True

    def is_one(self):
        """判断整个无向图中的所有节点是否连通 """
        temp = self.find_pre(self.start)
        for i in range(self.start+1, self.n+1):
            if self.find_pre(i) != temp:
                return False
        return True


class Kruskal:
    """Kruskal算法：求解无向连通图中的最小生成树 """
    def __init__(self, n, m):
        self.n = n  # n,m分别表示输入的点和边的个数
        self.m = m
        self.cost = 0
        self.node = [0 for i in range(n + 1)]  # 存放所有节点之间的可达关系与距离
        self.e = []  # 存放录入的无向连通图的所有边
        self.s = []  # 存放最小生成树里的所有边
        self.u = UnionFindSet(1, self.n)  # 并查集：抽象实现Graphnew，并完成节点间的连接工作以及判断整个图是否连通

    def create(self):
        # print(self.node)
        for i in range(1, self.n):
            for j in range(i+1, self.n+1):
                self.e.append(Edge(i, j, math.sqrt((self.node[i].x - self.node[j].x) ** 2 + (self.node[i].y - self.node[j].y) ** 2) + (self.node[i].cost - self.node[j].cost) ** 2))

    def graphy(self):
        """这里只是存储所有边的信息并按边的长度排序"""
        for i in range(1, self.n+1):
            x, y, h = list(map(int, input().split()))
            self.node[i] = Edge(x, y, h)
        self.create()
        self.e.sort(key=lambda e: e.cost)
        # for i in self.e:
        #     print(i.h)
        self.u.init()

    def run(self):
        """执行函数：求解录入的无向连通图的最小生成树 """
        for i in range(self.m):
            if self.u.unite(self.e[i].x, self.e[i].y):
                self.s.append(self.e[i])
            if self.u.is_one():
                """一旦Graphnew的连通分支数为1，则说明求出了最小生成树 """
                break

    def print(self):
        print(f'构成最小生成树的边为：')
        edge_sum = 0
        for i in range(len(self.s)):
            print(f'边 <{self.s[i].x},{self.s[i].y}> = {self.s[i].cost}')
            edge_sum += self.s[i].cost
        print(f'最小生成树的权值为：{edge_sum}')

def main():
    n = int(input())
    m = int((n * (n - 1)) / 2)
    kruskal = Kruskal(n, m)
    kruskal.graphy()
    kruskal.run()
    kruskal.print()

if __name__ == '__main__':
    main()





