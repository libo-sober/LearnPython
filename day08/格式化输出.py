# %s format
# name = '李波'
# age = 18
# msg = '我叫%s，今年%s' % (name, age)
# msg1 = '我叫{},今年{}'.format(name, age)
# print(msg, msg1)

# 新特性：格式化输出
# name = '李波'
# age = 18
# msg = f'我叫{name}，今年{age}'
# print(msg)
# 可以加表达式
# dic = {'name':'alex', 'age':73}
# lis = ['alex', 18]
# msg = f'我叫{dic["name"]},今年{dic["age"]}'
# msg1 = f'我叫{lis[0]},今年{lis[1]}'
# print(msg)
# print(msg1)
# count = 7
# print(f'最终结构：{count * 2}')
# name = 'barry'
# msg = F'我的名字是{name.upper()}'
# print(msg)
# 结合函数写
# def sum_(a, b):
#     return a + b
# msg = f'最终的计算结果是：{sum_(10, 20)}'
# print(msg)
# ！ ， ： {} : 这些标点不能出现在{}里面。
# 优点：
# 1. 结构更清晰，更简化。
# 2. 可以结合表达式以及函数使用。
# 3. 效率提升很多。

"""迭代器"""
# 获取一个对象的所以方法：dir()
# s1 = 'sdsdasasdas'
# # print(dir(s1))
# l1 = [1,2,3]
# print(dir(l1))
# print('__iter__' in dir(l1))  # True
#
# l1 = [1,2,3,4]
# for i in l1:
#     print(i)

# with open('wenjian', encoding='utf-8', mode='w') as f1:
#     print('__iter__' in dir(f1) and '__next__' in dir(f1)) # True
# # 可迭代对象可以转化成迭代器
# s1 = 'dasdasdas'
# # obj = iter(s1)  # s1.__iter__()
# # # print(obj)  # <str_iterator object at 0x0000022770E5EB70>
# # print(next(obj))  # d
# # print(obj.__next__())  # a
# #
# # l1 = [11,22,33,44,55]
# # obj = l1.__iter__()
# # print(obj.__next__())
# # print(obj.__next__())
# # print(obj.__next__())
# # print(obj.__next__())
# # print(obj.__next__())

# 迭代器会记住你的迭代位置
# l1 = [1,2,3,4,5,6,7,8]
# obj = l1.__iter__()
# for i in range(4):
#     print(next(obj))
#     1
#     2
#     3
#     4
# for i in range(3):
#     print(obj.__next__())
#     5
#     6
#     7
# while循环模拟for循环机制
l1 = [1,2,3,4,5,6,7,8]
# for i in l1:  # 先转换成迭代器
#     print(i)
# 将可迭代对象转换成迭代器
obj = l1.__iter__()
while True:
    try:
        print(next(obj))
    except StopIteration:
        break
