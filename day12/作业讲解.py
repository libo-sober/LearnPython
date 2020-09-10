# def wraper(f):
#     def inner(*args, **kwargs):
#         """执行被装饰函数之前的操作"""
#         print(111)
#         ret = f(*args, **kwargs)
#         """执行被装饰函数之后的操作"""
#         print(222)
#         return ret
#     return inner
#
#
# @wraper
# def func():
#     print('in func')
#
#
# func()  # func = wrapper(func)
# # 111
# # in func
# # 222

# def wraper(f):
#     def inner(*args, **kwargs):
#         """每次执行被装饰函数之前"""
#         print(111)
#         ret = f(*args, **kwargs)
#         """执行被装饰函数之后的操作"""
#         print(222)
#         return ret
#     return inner

# 为函数写一个装饰器，把函数的返回值 +100 然后再返回


# def wraper(f):
#     def inner(*args, **kwargs):
#         ret = f(*args, **kwargs)
#         return ret + 100
#     return inner
#
#
# @wraper  # func = wrapper(func)
# def func():
#     return 7
#
#
# result = func()  # inner()
# print(result)

# 请实现一个装饰器，通过一次调用是函数使函数重复执行5次。
# def wraper(f):
#     def inner(*args, **kwargs):
#         for i in range(5):
#             f(*args, **kwargs)
#     return inner
#
#
# @wraper  # func = wrapper(func)
# def func():
#     print('in func')
#
#
# func()
# # in func
# # in func
# # in func
# # in func
# # in func

# 请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。
import time
struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%S",struct_time))  # 当前时间节点
def wraper(f):
    def inner(*args, **kwargs):
        with open('log', mode='a', encoding='utf-8') as f1:
            f1.write(f'北京时间：{time.strftime("%Y-%m-%d %H:%M:%S",struct_time)}执行了{f.__name__}函数\n')
        ret = f(*args, **kwargs)
    return inner

@wraper
def wcnb():
    print('in func')

wcnb()
time.sleep(10)
wcnb()
time.sleep(5)
wcnb()
