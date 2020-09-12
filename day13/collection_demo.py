"""
collections模块

namedtuple():命名元组。
defaultdict():默认值字典。
Counter():计数器。
"""
from collections import namedtuple, defaultdict, Counter
# # nameedtuple()
# Rectangle = namedtuple('Rectangle', ['length', 'width'])
# # 通过属性访问元组的元素
# r = Rectangle(10, 5)
# print(r.length)  # 10
# print(r.width)  # 5
# # 通过索引方式
# print(r[0], r[1])

# 创建一个字典的方式
# d = {'name':'Andy'}
# d = dict([('name', 'Andy'), ('age', 10)])
# d = {k:v for k, v in [('name', 'Andy'), ('age', 10)]}
# print(d)
# defaultdict
# d = defaultdict(int, name='Andy', age=10)
# print(d['name'])  # Andy
# print(d['age'])  # 10
# print(d['addr'])  # 0  {'addr':0} 也会被添加
# print(d)  # defaultdict(<class 'int'>, {'name': 'Andy', 'age': 10, 'addr': 0})

# 自定义函数充电第一个参数
# def f():
#     return 'hello'
# d = defaultdict(f, name='Andy', age=10)
# print(d['addr'])  # hello
# print(d)  # defaultdict(<function f at 0x00000176EEE11EA0>, {'name': 'Andy', 'age': 10, 'addr': 'hello'})

# Counter:计数器
c = Counter('adasdasnadasada')
print(c)  # Counter({'a': 7, 'd': 4, 's': 3, 'n': 1})
print(c.most_common(3))  # [('a', 7), ('d', 4), ('s', 3)]  前3个







