# 装饰器：装饰，装修，房子就可以住，如果装修，不影响你住，而且体验更加，
# 让你生活中增加； 很多功能，洗澡，看电视
# 器：工具。
# 开放封闭原则：
# 开放：对代码的扩展是开放的。
# 封闭：对源码的修改是封闭的。
# 装饰器：完全遵循开放封闭原则。
# 装饰器：在不改变原函数代码以及调用方式的前提下给其增加新的功能。
# 装饰器就是一个函数。
#
# 版本一：A 写一些代码，测试一下index函数的执行效率。
# def index():
#     """有很多代码"""
#     time.sleep(2)  # 模拟的网络延迟
#     print('欢迎登录博客园首页')
#
# def dariy():
#     """有很多代码"""
#     time.sleep(3)  # 模拟的网络延迟
#     print('欢迎登录博客园日记首页')
#
# # 如果测试别人的代码，要重复复制
# import time
# # print(time.time())  # 格林尼治时间。 1599562276.1415439
# star_time = time.time()
#
# index()
#
# end_time = time.time()
# print(end_time - star_time)
# 版本2：利用函数，解决代码重复使用问题
# import time
# def index():
#     """有很多代码"""
#     time.sleep(2)  # 模拟的网络延迟
#     print('欢迎登录博客园首页')
#
# def dariy():
#     """有很多代码"""
#     time.sleep(3)  # 模拟的网络延迟
#     print('欢迎登录博客园日记首页')
#
# def timmer(f):
#
#     star_time = time.time()
#
#     f()
#
#     end_time = time.time()
#     print(end_time - star_time)
#
#
# timmer(index)
# 版本二还是有问题：原来index函数源码没有改变，给原函数添加了一个新的功能，
# 测试原函数效率的功能。满足开放封闭原则？原函数的调用方式改变了

# 版本三：不能改编原函数的调用方式。
# import time
# def index():
#     """有很多代码"""
#     time.sleep(2)  # 模拟的网络延迟
#     print('欢迎登录博客园首页')
#
# def dariy():
#     """有很多代码"""
#     time.sleep(3)  # 模拟的网络延迟
#     print('欢迎登录博客园日记首页')
#
# def timmer(f):
#
#     def inner():
#         star_time = time.time()
#         f()
#         end_time = time.time()
#         print(end_time - star_time)
#
#     return inner
#
#
# # timmer(index)  # index()
# # ret = timmer(index)   # inner
# # ret()  # inner()
# """最基础的装饰器"""
# index = timmer(index)  # inner
# index()  # inner()

# def func():
#     print('in func')
# def func1():
#     print('in func1')
#
# func()
# func = 666
# func()  # TypeError: 'int' object is not callable

# 版本四：继续研究
# import time
# def index():
#     """有很多代码"""
#     time.sleep(2)  # 模拟的网络延迟
#     print('欢迎登录博客园首页')
#
# def timmer(f):
#     # f = index
#     def inner():
#         star_time = time.time()
#         f()
#         end_time = time.time()
#         print(end_time - star_time)
#
#     return inner
#
#
# index = timmer(index)
# index()

# 版本五：python做了一个优化：提出了一个语法糖的概念。
# @装饰器名
# 标准版的装饰器
# import time
# # 装饰器写在最上面
# # timmer装饰器
# def timmer(f):
#     # f = index
#     def inner():
#         star_time = time.time()
#         f()
#         end_time = time.time()
#         print(end_time - star_time)
#
#     return inner
#
#
# @timmer  # index = timmer(index)
# def index():
#     """有很多代码"""
#     time.sleep(0.6)  # 模拟的网络延迟
#     print('欢迎登录博客园首页')
#     return 666
#
#
# @timmer  # dariy = timmer(dariy)
# def dariy():
#     """有很多代码"""
#     time.sleep(0.3)  # 模拟的网络延迟
#     print('欢迎登录博客园日记首页')

#
# # index = timmer(index)
# # index()
#
# # dariy = timmer(dariy) @timmer
# # dariy()
#
# ret = index()
# print(ret)  # None 有返回值 不行啦？
#
# dariy()

# 版本六：被装饰函数有返回值
# import time
# # 装饰器写在最上面
# # timmer装饰器
# def timmer(f):
#     # f = index
#     def inner():
#         star_time = time.time()
#         r = f()  # 把返回值给他返出去再
#         # print(f'真正的index函数返回值{f()}')  # index()
#         end_time = time.time()
#         print(end_time - star_time)
#         return r
#
#     return inner
#
#
# @timmer  # index = timmer(index)
# def index():
#     """有很多代码"""
#     time.sleep(0.6)  # 模拟的网络延迟
#     print('欢迎登录博客园首页')
#     return 666
#
#
# # 加上装饰器不应该改变原函数的返回值，所以666应该返回给我下面的ret
# # 但是下面这个ret实际接收的是inner函数的返回值，而666返回给的是装饰器里面的
# # f()，也就是r,我们现在要解决的问题就是将r给inner的返回值。
# ret = index()
# print(ret)

# 版本七: 最标准版的装饰器。
import time
# 装饰器写在最上面
# timmer装饰器
def timmer(f):
    # f = index
    def inner(*args, **kwargs):
        # 函数的定义：* 聚合 args=('李素琴', 18)
        star_time = time.time()
        r = f(*args, **kwargs)  # 把返回值给他返出去再
        # 函数的执行：* 打散：f(*iterable) --> f(*('李素琴', 18)) --> f('李素琴', 18)
        # print(f'真正的index函数返回值{f()}')  # index()
        end_time = time.time()
        print(end_time - star_time)
        return r

    return inner


@timmer  # index = timmer(index)
def index(name):
    """有很多代码"""
    time.sleep(0.6)  # 模拟的网络延迟
    print(f'欢迎{name}登录博客园首页')
    return 666


@timmer  # dariy = timmer(dariy)
def dariy(name, age):
    """有很多代码"""
    time.sleep(0.3)  # 模拟的网络延迟
    print(f'欢迎{age}岁的{name}登录博客园日记首页')


dariy('李素琴', 18)  # inner(name, age)

index('那亲')  # inner('那亲')


# 标准版的装饰器


def wrapper(f):
    def inner(*args, **kwargs):
        """添加额外的功能：执行被装饰函数之前的操作"""
        ret = f(*args, **kwargs)
        """添加额外的功能：执行被装饰函数之后的操作"""
        return ret
    return inner
