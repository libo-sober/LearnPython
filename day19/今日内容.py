"""
模块和实际工作时间的关系

正则表达式  *****

re模块

自动化运维---开发
爬虫

"""
"""
Prim类接受两个参数n,m，分别表示录入的点和边的个数（点的编号从1开始递增）
接下来是m行，每行3个数x,y,length，表示点x和点y之间存在一条长度为length的边 
程序最终会打印出该无向图中的最小生成树的各个边和最小权值 
"""
import math

class Node:
    """
    Node类存放节点信息，
    node是与某个节点（实际上是用列表索引值代表的）相连接的点
    length表示这两个点之间的权值
    """
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h


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


class Prim:
    """Prim算法：求解无向连通图中的最小生成树 """
    def __init__(self, n, adj_map):
        self.n = n  # 输入的点个数
        self.adj_map = adj_map
        self.cost = 0
        self.node = [0 for i in range(n + 1)]  # 存放所有节点之间的可达关系与距离
        """图的邻接表的表示法，v是一个二维列表，其索引值代表当前节点，索引值对应的一维列表中存放的
        是与以当前索引值为顶点的相连的节点信息"""
        self.e = []  # 存放输入节点
        self.vis = [False for i in range(n+1)]  # 标记每个点是否被访问过，False未访问

    def create(self):
        for i in range(1, self.n):
            for j in range(i+1, self.n+1):
                self.adj_map[i][j] = self.adj_map[j][i] = math.sqrt((self.node[i].x - self.node[j].x) ** 2 + (self.node[i].y - self.node[j].y) ** 2) + (self.node[i].h - self.node[j].h) ** 2

    def graphy(self):
        """构建图，这里用的是邻接表"""
        for i in range(1, self.n+1):
            x, y, h = list(map(int, input().split()))
            self.node[i] = Node(x, y, h)
        self.create()

    def insert(self, point):
        self.vis[point] = True
        for i in range(1, self.n+1):
            if not self.vis[i]:
                self.e.append(Edge(point, i, self.adj_map[point][i]))
        self.e = sorted(self.e, key=lambda e: e.cost)  # 把e中的所有边按边的长度从小到大排序
        # for i in self.e:
        #     print(i.cost, i.x, i.y)

    def run(self, start):
        """执行函数：求解录入的无向连通图的最小生成树"""
        self.insert(start)  # start为选择的开始顶点
        selected = 1
        # exit()
        while selected < self.n:
            for i in range(len(self.e)):
                if not self.vis[self.e[i].y]:
                    self.cost += self.e[i].cost
                    self.insert(self.e[i].y)
                    selected += 1
                    break
        return self.cost


def main():
    n = int(input())
    adj_map = [[0] * (n+1) for i in range(n+1)]
    prim = Prim(n, adj_map)
    prim.graphy()
    # print(adj_map)
    cost = prim.run(1)
    print(round(cost, 2))


if __name__ == '__main__':
    main()
