# def func():
#     print(666)
# 1. 函数名指向的是函数的内存地址。
# 函数名加上括号就能执行此函数
# a = 1
# a()  # 报错
# func()
# a = {'name':'alex'}
# b = {'age':18}
# print(a + b) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# a = 1
# b = 2
# print(a + b)
# print(func, type(func))  # <function func at 0x000002025BC31EA0> <class 'function'>
# # 2. 函数名就是变量。
# a = 2
# b = a
# c = b
# print(b)
# f = func
# f2 = f
# f2()
# f()
# func()
# def func():
#     print('in func')
# def func1():
#     print('in func1')
# func1 = func
# func1()  # in func
# 3. 函数名可以作为容器类数据类型的元素
# def func1():
#     print('in func1')
#
# def func2():
#     print('in func2')
#
# def func3():
#     print('in func3')
# l1 = [func1, func2, func3]
# for i in l1:
#     i()
# 4. 函数名可以作为函数的参数
# def func():
#     print('in func')
# def func1(x):
#     x()  # func()
#     print('in func1')
# func1(func)
# 5. 函数名可以作为函数的返回值
# def func():
#     print('in func')
# def func1(x):
#     print('in func1')
#     return x
# ret = func1(func)
# ret()
# in func1
# in func

