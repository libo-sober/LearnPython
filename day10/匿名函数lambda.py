# # 匿名函数，也叫一句话函数，比较简单。
# def func(a, b):
#     return a + b
# # 构建匿名函数
# func1 = lambda a, b: a + b
# print(func(1, 2))
# print(func1(1, 2))
# # 格式
# # lambda 形参:返回值
# # 接收一个可切片的数据，返回索引为0与2的对应的元素（元组形式）。
# func2 = lambda lst: lst[0:3:2]
# print(func2([1,2,3,4,5,6]))
# # 写匿名函数，接收两个int参数，将较大的数据返回。
# func3 = lambda a,b: a if a > b else b
# print(func3(3,9))


# # 内置函数
# # int
# print(int(3.6))  # 3
#
# # complex 复数
# print(complex(1, 2))  # (1+2j)
#
# # bin:将十进制转成2进制
# print(bin(100))  # 0b1100100
#
# # oct:将十进制转换成八进制
# print(oct(100))  # 0o144
#
# # hex:将十进制转换成十六进制
# print(hex(100))  # 0x64
#
# # divmod: 返回一个列表，列表中值为(商， 余数)
# print(divmod(10, 3))  # (3, 1)
#
# # round:保留浮点数小数位数，并且四舍五入
# print(round(3.1415926, 3))  # 3.142
#
# # pow:求x**y次幂。（三个参数为x**y的结果对z取余）。
# print(pow(2, 3))  # 8
# print(pow(2, 3, 3))  # 2
#
# # bytes:
# s1 = '太白'
# b = s1.encode('utf-8')
# print(b)  # b'\xe5\xa4\xaa\xe7\x99\xbd'
# b = bytes(s1, encoding='utf-8')
# print(b)  # b'\xe5\xa4\xaa\xe7\x99\xbd'
#
# # ord:输入字符找该字符编码的位置。
# print(ord('a'))  # 97  ASCII码
# print(ord('亚'))  # 20122  Unicode
# # chr:输入位置数字找出器对应的字符。
# print(chr(97))  # a  ASCII码
# print(chr(20122))  # 亚   Unicode
#
# # repr:返回一个对象的string形式（原形毕露）
# s1 = '太白'
# print(s1)  # 太白
# print(repr(s1))  # '太白'
# msg = '我叫%s' % s1
# print(msg)  # 我叫太白
# msg1 = '我叫%r' % s1
# print(msg1)  # 我叫'太白'
#
# # all:可迭代对象中，全都是True才是True
# l1 = [1, 2, 3, '']
# print(all(l1))  # False
#
# # any: 可迭代对象中，有一个True就是True。
# print(any(l1))  # True
#
# # print  def print(self, *args, sep=' ', end='\n', file=None):
# print(1,2,3,4,5,sep='&', end='###')  # 1&2&3&4&5###
# print()
# # list
# l2 = list('12345')
# print(l2)  # ['1', '2', '3', '4', '5']
#
# # dict 创建字典的集中的方式
# # 直接创建
# # 元组的结构
# # 键值对
# # fromkeys
# # update
# # 字典推导式
# dic = dict([(1, 'one'), (2, 'two'), (3, 'three')])
# print(dic)   # {1: 'one', 2: 'two', 3: 'three'}
# print(dict(one = 1, two = 2))  # {'one': 1, 'two': 2}
#
# # abs：绝对值
# print(abs(-78))  # 78
#
# # sum: 求和
# print(sum([i for i in range(10)]))  # 45
# print(sum([i for i in range(10)], 100))  # 145,设置初始值为100
#
# # reversed：对原列表反转。
# l3 = [i for i in range(10)]
# l3.reverse()  #列表的方法
# print(l3)
# obj = reversed(l3)  # obj是一个迭代器。
# print(list(obj))  # 源列表不会改变，产生一个新的原列表反转的迭代器
#
# # zip 拉链方法
# l4 = [1,2,3,4,5]
# tul = ('太白', 'b哥', '德刚')
# s2 = 'abcd'
# obj2 = zip(l4, tul, s2)  # 一个生成器对象
# print(obj2)  # <zip object at 0x0000025FDB48EE48>
# # for i in obj2:
# #     print(i)
# # (1, '太白', 'a')
# # (2, 'b哥', 'b')
# # (3, '德刚', 'c')
# print(list(obj2))
# # [(1, '太白', 'a'), (2, 'b哥', 'b'), (3, '德刚', 'c')]


# 一下方法非常重要
# min max
# l1 = [33, 3,5,76,29, -1, -9]
# print(min(l1))  # -9
# # 以绝对值的方式去最小值
# l2 = []
# func = lambda a:abs(a)
# for i in l1:
#     l2.append(func(i))
# print(min(l2))  # 1
# min() def min(*args, key=None):
# def abss(a):
#     return abs(a)
# print(min(l1, key=abss))  # 输出-1
# print(abs(min(l1,key=abss))) # key=函数名  返回1
# # 凡是可以加key的：它会自动的将可迭代对象中的每个元素按照顺序传入key对应的函数中，
# # 以返回值比较大小。
# dic = {'a': 3, 'b': 2, 'c': 1}
# # 求出值最小的键值对
# print(dic['a'])
# print(min(dic))   # a  min默认会按照字典的键去比较大小。
# print(min(dic,key=lambda a: dic[a]))  # C
# """
# 第一次：
# a: 'a'  返回值：dic['a'] 记录：3
# 第二次：
# a: 'b'  返回值：dic['b'] 记录：2
# 第三次：
# a: 'c'  返回值：dic['c'] 记录：1
# """
# # 找年龄最小的
# l2 = [('太白',18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
# print(min(l2))  # ('alex', 73)
# print(min(l2, key=lambda lst: lst[1]))  # ('太白', 18)

# max 一样

# sorted 排序
# l1 = [22, 33, 1, 2, 7, 4]
# l2 = sorted(l1)
# # print(l2)   # [1, 2, 4, 7, 22, 33]
# l2 = [('太白',18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
# print(sorted(l2))  # [('alex', 73), ('wusir', 35), ('口天吴', 41), ('太白', 18)]
# print(sorted(l2, key=lambda x:x[1]))  # 返回的是一个列表  [('太白', 18), ('wusir', 35), ('口天吴', 41), ('alex', 73)]
# print(sorted(l2, key=lambda x:x[1], reverse=True))  # 从大到小
#
# # filter 列表推导式的筛选模式
# l1 = [2, 3, 4, 5, 77, 3]
# print([i for i in l1 if i > 3])
# ret = filter(lambda x: x > 3, l1)
# print(ret)
# print(list(ret))
# # [4, 5, 77]
# # <filter object at 0x000001C4B1BFEC50>
# # [4, 5, 77]

# map  列表推导式的循环模式
# l1 = [1, 4, 9, 16, 25]
# print([i ** 2 for i in range(1, 6)])
# ret = map(lambda x:x**2,range(1, 6))
# print(ret)
# print(list(ret))
# [1, 4, 9, 16, 25]
# <map object at 0x0000018E50A0EC50>
# [1, 4, 9, 16, 25]

# reduce
from functools import reduce
def func(x, y):
    """
    第一次：x y : 11 2    x + y =  记录：13
    第二次：x = 13 y = 3  x + y =       16
    第三次：x = 16 y = 4  x + y =       20
    :param x:
    :param y:
    :return:
    """
    return x + y
l = reduce(func, [11,2,3,4])
print(l)  # 20


