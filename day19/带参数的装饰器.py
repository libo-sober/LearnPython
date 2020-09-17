"""
什么是装饰器？
开放封闭原则
我们提前写好一个功能，让别人使用的时候能够直接使用就能完成相应的功能
"""
# 登录
# 计算函数的执行时间
# 写了很多的函数
# 添加日志： 在  时间  调用了什么函数
import time

# print(f'北京时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
# # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
def logger(path):
    def log(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            with open(path, mode='wt', encoding='utf-8') as f:
                msg = f"{time.strftime('%Y-%m-%d %H:%M:%S')} 执行了 {func.__name__}"
                f.write(msg)
            return ret

        return inner

    return log
#

@logger('auth.log')  # ret = log('auth.log') login = ret(login)
def login():
    print('登录')
@logger('auth.log')
def register():
    print('注册')
@logger('operate.log')  # 必须传参 不传参报错
def show():
    print('查看')
@logger('operate.log')
def add_goods():
    print('加购')


login()
add_goods()
show()

# 登录和注册的信息写到auth.log文件里
# 所以的购物信息 写道operate.log文件中
# @log   # login = log(login)
# def login():
#     print('登录')
#
# @log('auth.log')  # log('auth.log') --> ret login = ret(login)
# def login():
#     print('登录')
# # 标准带参装饰器
# def xxx(*args, **kwargs):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             """func执行前的操作"""
#             """可以对*args和**kwargs操作"""
#             ret = func(*args, **kwargs)
#             """可以对*args和**kwargs操作"""
#             """func执行后的操作"""
#             return ret
#         return inner
#     return wrapper
# 有100个函数，分别添加一个计算函数执行时间的装饰器
# 有的时候需要计算时间，有的时候不需要
# 希望能通过修改一个变量，能控制着100个函数的装饰器是否执行


