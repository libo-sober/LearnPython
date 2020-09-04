# 封闭的东西：保证数据的安全。

# 方案1
# l1 = []  # 全局变量
# li = []
# def maker_average(new_value):
#     l1.append(new_value)
#     return sum(l1) / len(l1)
# print(maker_average(100000))
# print(maker_average(110000))
# # 很多代码
# l1.append(666)  # 误用l1
# print(maker_average(120000))
# print(maker_average(90000))

# 方案2：数据安全，l1不能说全局变量。
# 每次执行时l1的列表都会重新赋值为空列表。
# li = []
# def maker_average(new_value):
#     l1 = []
#     l1.append(new_value)
#     return sum(l1) / len(l1)
# print(maker_average(100000))
# print(maker_average(110000))
# # 很多代码
# print(maker_average(120000))
# print(maker_average(90000))

# 方案3：闭包。

# def maker_average():
#     l1 = []
#     def average(new_value):
#         l1.append(new_value)
#         return sum(l1) / len(l1)
#     return average
#
#
# avg = maker_average()  # average
# print(avg.__code__.co_freevars)  # ('l1',)
# print(avg(100000))
# print(avg(110000))
# print(avg(120000))
# print(avg(90000))
# 全局
# maker_average:地址1
# avg: 地址2
# 临时名称空间
# l1 = []
# average: 地址2

# 闭包：  多用于面试题：什么是闭包？闭包有什么作用？
# 1. 闭包只能存在嵌套函数中。
# 2. 内层函数对外层函数非全局变量的引用（使用），就会形成闭包。
# 被引用的非全局变量也称作自由变量，这个自由变量就会与内层函数产生一个绑定关系，
# 自由变量不会在内层中消失。
# 闭包的作用：保证程序的安全性。

# 如何判断一个嵌套函数是不是闭包？
# 1. 闭包只能存在嵌套函数中。
# 2. 内层函数对外层函数非全局变量的引用（使用），就会形成闭包。
# 例一：
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     return inner
# ret = wrapper()
# 是
# 例二：
# a = 2
# def wrapper():
#     def inner():
#         print(a)
#     return inner
# ret = wrapper()
# 不是
#
# # 例三：
#
# def wrapper(a,b):
#     def inner():
#         print(a)
#         print(b)
#     return inner
# a = 2
# b = 3
# ret = wrapper(a,b)
# 是

# 如何用代码判断闭包
def wrapper(a,b):
    def inner():
        print(a)
        print(b)
    return inner
a = 2
b = 3
ret = wrapper(a,b)
print(ret.__code__.co_freevars)  # ('a', 'b') 有两个自由变量

