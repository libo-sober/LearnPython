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

import sys
def prim(graph,n):
    '''
    prim算法求最小生成树
    :param graph: 图
    :return: 最小的权值
    :n:点的个数
    '''
    lowcost = []
    mst = []
    cost = 0
    for i in range(n):
        lowcost.append(graph[0][i])
        mst.append(0)
    v = 0
    lowcost[0] = -1
    for i in range(n-1):
        min = sys.maxsize
        for j in range(n):
            if(min > lowcost[j] and lowcost[j] != -1):
                min = lowcost[j]
                v = j
        cost += min
        print(traver(mst[v]),"->",traver(v),": ",min)
        lowcost[v] = -1
        for k in range(n):
            if(lowcost[k] > graph[v][k]):
                lowcost[k] = graph[v][k]
                mst[k] = v

    return cost

def traver(x):
    '''
    把数字转换为字母
    只使用与26个小写字母
    :param x: 待转换数字
    :return: 字母
    '''
    return chr(x+97)


if __name__=='__main__':
    MAX = sys.maxsize
    '''知乎上举例所用的图'''
    graph = [[MAX,6,1,5,MAX,MAX],
             [6,MAX,5,MAX,3,MAX],
             [1,5,MAX,5,6,4],
             [5,MAX,5,MAX,MAX,2],
             [MAX,3,6,MAX,MAX,6],
             [MAX,MAX,4,2,6,MAX]]
    print(prim(graph,len(graph)))



