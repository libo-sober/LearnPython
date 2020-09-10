# 仅限关键字参数
# def func(a, b, *args,c):
#     print(a, b)
#     print(args)
#     print(c)
#
#
# func(1,2,3,4,c=5)
#
# *
# a, b = (1, 2)
# a, b, *c = (1,2,3,4,5,6,7,8)
# print(a,b,c)  #1 2 [3, 4, 5, 6, 7, 8]
#
# a, *b, c = [11,22,33,44,55,66,77]
# print(a, b, c)  # 11 [22, 33, 44, 55, 66] 77
#
# a, *b = range(10)
# print(a, b)  # 0 [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def func():
#     global name
#     name = 'alex'
#
# func()
# print(name)  # NameError: name 'name' is not defined
# def func():
#     global name
#     name = 'alex'
# print(name)  # NameError: name 'name' is not defined  函数未执行 找不到
# func()
# print(name)  # 可以找到
# name = '太白'
# def func():
#     global name
#     name = 'alex'
# print(name)  # 太白
# func()
# print(name)  # alex
#
# def func():
#     name = '太白'
#     def inner():
#         nonlocal name
#         name = 'alex'
#     print(name)
#     inner()
#     print(name)
#
# func()
# # 太白
# # alex
def wrapper(a):
    name = '太白'

    def inner():
        print(a)
        print(name)

    return inner


ret = wrapper('烧饼')

print(ret.__code__.co_freevars)  # ('name',)
# print(name) 访问不到

def wrapper(f):
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)
        return ret
    return inner