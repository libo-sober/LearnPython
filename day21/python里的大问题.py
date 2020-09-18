"""
命名空间和内存
组合
"""
# 类：这个类有什么属性 用什么方法 大致的样子
# 不能知道具体的属性对应的值
# 对象：之前所有的属性值就都明确了
# 类型 int float str dict list  ---类
# python中一切皆对象，对象的类型就是类

class A(object):
    def __init__(self):
        pass
    def func(self):
        print('func')

a = A()
a.func()
# 类中的静态变量的用处
# 如果一个变量 是所有的对象共享的值，那么这个变量应该
# 被定义成静态变量，所有和静态相关的增删都应该使用类名来处理



