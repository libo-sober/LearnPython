"""
面试常考题目：

默认参数的陷阱:
    陷阱值针对与默认参数是可变的数据类型

如果你的默认参数指向的是可变的数据类型，那么你无论调用多少次这个默认参数，都是同一个

"""


# def func(name, alist=[]):
#     alist.append(name)
#     return alist
#
# 如果你的默认参数指向的是可变的数据类型，那么你无论调用多少次这个默认参数，都是同一个
# # alist 不在全局，也不再局部，在一个特殊的地方，不会随着第一次函数的消失
# ret1 = func('alex')  # ['alex'] 2455746845320
# print(ret1, id(ret1))
# ret2 = func('效力')  # ['alex', '效力'] 2455746845320
# print(ret2, id(ret2))

# def func(a, list= []):
#     list.append(a)
#     return list
# print(func(10,))  # [10]
# print(func(20,[]))  # [20] 传入了1个新的空列表
# print(func(100,))  # [10, 100] 沿用之前的列表
# def func(a, list= []):
#     list.append(a)
#     return list
# ret1 = func(10,)
# ret2 = func(20,[])
# ret3 = func(100,)
# print(ret1)  # [10, 100]  ret1和ret3是同一个列表
# print(ret2)  # [20]
# print(ret3)  # [10, 100]  ret1和ret3是同一个列表
# count = 1
# def func():
#     count += 1  # 报错
#     print(count)
# func()
#
# 在函数中 如果你定义了一个变量，但是在定义这个 变量之前对其引用了，那么解释器人为：语法问题。
# 你应该在使用之前先定义。
# count = 1
# def func():
#     print(count)# 报错  在局部函数中先引用后定义了 所以报错
#     count = 3
# func()

# global nonlocal
"""
global
1.在局部作用域生命一个全局变量。
2.在全局照样能用，集使全局没有这个变量。但是必须函数执行后才可以用，否则找不到这个变量。
3. 修改一个全局变量。在局部对全局变量进行修改。
"""
# name = 'alex'
# def func():
#     name = '摇摆'
#     print(name)
# func() 摇摆
# print(name) alex
# name = 'alex'
# def func():
#     global name
#     name = '摇摆'
#     print(name)
# func() 摇摆
# print(name) 摇摆
# def func():
#     global name
#     name = '摇摆'
#     print(name)
# func() 摇摆
# print(name) 摇摆
# def func():
#     global name
#     name = '摇摆'
#     print(name)
# print(name)  # 函数还没有执行，找不到name,会报错
# func()

"""
nonlocal
1. 不能够操作全局变量。
2. 局部作用域：内层函数对外层函数的局部变量进行修改。
"""
# count = 1
# def func():
#     nonlocal count
#     count += 1
#     print(count)
# func() SyntaxError: no binding for nonlocal 'count' found
count = 1
# def wrapper():
#     count = 1
#     def inner():
#         count += 1  # 报错
#     inner()
def wrapper():
    count = 1
    def inner():
        nonlocal count
        count += 1  # 这样可以操作count
    print(count)
    inner()
    print(count)
wrapper()
