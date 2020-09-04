# # 构建一个列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期',
# # 'python8期', 'python9期', 'python10期']
# lst = [f'python{i}期' for i in range(1, 11) if i != 5]
# print(lst)
# # 构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# lst2 = [(i, i + 1) for i in range(6)]
# print(lst2)
# # 构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# lst3 = [i for i in range(0, 20, 2)]
# print(lst3)
# # 有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']
# # 将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
# l1 = ['alex', 'WuSir', '老男孩', '太白']
# lst4 = [l1[i] + f'{i}' for i in range(4)]
# print(lst4)
# # 将下面这个列表
# x = {'name': 'alex',
#      'values': [{'timestamp': 151799.43, 'values': 100},
#                 {'timestamp': 253459.43, 'values': 200},
#                 {'timestamp': 351799.43, 'values': 300},
#                 {'timestamp': 451799.43, 'values': 400},
#                 {'timestamp': 551799.43, 'values': 500},
#                 {'timestamp': 651799.43, 'values': 600}]}
# # 通过列表推导式转换成下面的类型：
# # [[151799.43, 100], [253459.43, 200], [351799.43, 300], [451799.43, 400],
# # [551799.43, 500], [651799.43, 600]]
# lst5 = [[dic['timestamp'], dic['values']] for dic in x['values']]
# print(lst5)
# # 用列表完成笛卡尔积
# # 什么是笛卡尔积？笛卡尔积就是一个列表，
# # 列表里面的元素是由输入的可迭代类型的元素对构成的元组，
# # 因此，笛卡尔积列表的长度等于输入变量的长度的乘积。
# # 构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# lst6 = [(size, color) for size in sizes for color in colors]
# print(lst6)
# # [('S', 'black'), ('S', 'white'), ('M', 'black'), ('M', 'white'), ('L', 'black'), ('L', 'white')]
# # 构建一个列表，列表里的元素是扑克牌去除大小王以后，所有的牌类
# kinds = ['spades', 'diamonds', 'clubs', 'hearts']
# pukes = list('A'+'23456789'+'10'+'JQK')
# lst7 = [(puke, kind) for puke in pukes for kind in kinds]
# print(lst7)
# # [('A', 'spades'), ('A', 'diamonds'), ('A', 'clubs'), ('A', 'hearts'), ('2', 'spades'), ('2', 'diamonds'), ('2', 'clubs'), ('2', 'hearts'), ('3', 'spades'), ('3', 'diamonds'), ('3', 'clubs'), ('3', 'hearts'), ('4', 'spades'), ('4', 'diamonds'), ('4', 'clubs'), ('4', 'hearts'), ('5', 'spades'), ('5', 'diamonds'), ('5', 'clubs'), ('5', 'hearts'), ('6', 'spades'), ('6', 'diamonds'), ('6', 'clubs'), ('6', 'hearts'), ('7', 'spades'), ('7', 'diamonds'), ('7', 'clubs'), ('7', 'hearts'), ('8', 'spades'), ('8', 'diamonds'), ('8', 'clubs'), ('8', 'hearts'), ('9', 'spades'), ('9', 'diamonds'), ('9', 'clubs'), ('9', 'hearts'), ('1', 'spades'), ('1', 'diamonds'), ('1', 'clubs'), ('1', 'hearts'), ('0', 'spades'), ('0', 'diamonds'), ('0', 'clubs'), ('0', 'hearts'), ('J', 'spades'), ('J', 'diamonds'), ('J', 'clubs'), ('J', 'hearts'), ('Q', 'spades'), ('Q', 'diamonds'), ('Q', 'clubs'), ('Q', 'hearts'), ('K', 'spades'), ('K', 'diamonds'), ('K', 'clubs'), ('K', 'hearts')]
# # 看下面的代码，能否对其简化？说说你简化后的优点？
# # def chain(*args):
# #     # ('abc', (0, 1, 2))
# #     for it in args:
# #         for i in it:
# #             yield i
# # g = chain('abc', (0, 1, 2))
# # 怎么让生成器产出值？
# # 1. next. 2. for循环. 3. 转化成list
# # print(next(g))  # a
# # print(list(g))  # ['b', 'c', 0, 1, 2]
# def chain(*args):
#     # ('abc', (0, 1, 2))
#     for it in args:
#         yield from it
# g = chain('abc', (0, 1, 2))
# print(next(g))  # a
# # yield from 优化了内层循环，提高了效率。
# # 看代码，求结果。
# v = [i % 2 for i in range(10)]
# print(v)  # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# v1 = (i % 2 for i in range(10))
# print(v1)  # 这是一个生成器，需要next才会产生值
# print(next(v1))

def demo():
    for i in range(4):
        yield i
g = demo()
print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

g1 = (i for i in g)
# print(g1)
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
g2 = (i for i in g1)
# print(g2)
print(list(g1))  # list 一次把生成器的所有内容接收掉并返回一个列表。
print(list(g2))  # 生成器输出完后变空。
# 生成器的随着next换值，取完后为空。
# 生成器里永远只有一个值，next一次后这个值丢弃，下一个值进来。
# [0, 1, 2, 3]
# []
def add(n, i):
    return n + i

def test():
    for i in range(4):
        yield i

g = test()
for n in [1, 10]:
    g = (add(n, i) for i in g)
    print(g)
# n = 1  g = (add(1, i) for i in test())  g = [1, 2, 3, 4] 错
# n = 10 g = (add(10, i) for i in test())  [10, 11, 12, 13] 错

# 两个g是不同的
# <generator object <genexpr> at 0x0000026DFF6B9780>
# <generator object <genexpr> at 0x0000026DFF6ED570>
# n = 1  g = (add(1, i) for i in [0,1,2,3])  g = [1, 2, 3, 4] 错
# n = 10 g = (add(10, i) for i in (add(10, i) for i in [0,1,2,3]))  [10, 11, 12, 13] 错
# list((add(10, i) for i in (add(10, i) for i in [0,1,2,3])))
# list((add(10, i) for i in [10, 11, 12, 13]))
# [20, 21, 22, 23]
print(list(g))
# a = range(1, 5)
# a = [i for i in a]
# a = [i ** 2 for i in a]
# print(a)
