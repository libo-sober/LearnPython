# # 用字符串数据类型的名字 来操作这个名字对应的函数/实例鸟朦胧/各种方法
# # name ='alex'
# # age = 123
#
# # n = input('>>>')
# # 有些时候你知道一个字符串数据类型的名字，你向直接掉用，但是钓不到
# # 使用反射
# # 1. 反射对象的 实例变量
# # 2。 反射一个类的静态变量/绑定方法/其他方法
# # 3. 模块中的所有变量
# #       被导入的模块
# #       当前执行的py文件
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def nihao(self):
#         print('nihapo')
# alex = Person('alex', 83)
# wusir = Person('wusir', 84)
# # print(alex.name)
# # print(wusir.name)
# ret = getattr(wusir, 'name')
# print(ret)
# # 通过字符串直接反射到对应的地址
# # 我们无法通过字符串来把他当作类名方法名调用，这样反射后就得到对应的地址
# class Payment:
#     pass
# class Alipay(Payment):
#     def __init__(self, name):
#         self.name = name
#     def pay(self, money):
#         dic = {'uname':'用户名','price':money}
#         # 想办法调用支付宝支付吧dic纯过去
#         print(f'{self.name}通过支付宝支付{money}成功')
#
# class WeChat(Payment):
#     def __init__(self, name):
#         self.name = name
#
#     def pay(self, money):
#         dic = {'uname': '用户名', 'price': money}
#         # 想办法调用支付宝支付吧dic纯过去
#         print(f'{self.name}通微信支付{money}成功')
#
# class QQpay(Payment):
#     def __init__(self, name):
#         self.name = name
#
#     def pay(self, money):
#         dic = {'uname': '用户名', 'price': money}
#         # 想办法调用支付宝支付吧dic纯过去
#         print(f'{self.name}通qq支付{money}成功')
#
# # ali = Alipay('小明')
# # ali.pay(300)
# import sys
# # 归一化设计
# def pay(name, price, way):
#     obj_name = getattr(sys.modules['__main__'], way)
#     obj = obj_name(name)
#     obj.pay(price)
#     # if way == 'WeChat':
#     #     obj = WeChat(name)
#     #     obj.pay(price)
#     # elif way == 'Alipay':
#     #     obj = Alipay(name)
#     #     obj.pay(price)
#
#
# pay('alex', 400, 'Alipay')
# pay('alex', 400, 'WeChat')
# pay('alex', 400, 'QQpay')
#
# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def nihao(self):
#         print('nihao ')
# a = A('li', 22)
# re = getattr(a, 'name')
# print(re)
# getattr(a, 'nihao')()
# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def func(self):
#         pass
# a = A('li', 22)
# print(hasattr(a, 'namw'))  # False
# print(hasattr(a, 'name'))  # True
# if hasattr(a, 'name'):
#     print(getattr(a, 'name'))
# callable()  # 判断一个东西是否能调用
# 作业1
# class Authentic:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def register(self):
#         print('注册')
#     def login(self):
#         print('登录')
# lst = [('登录', 'login'), ('注册', 'register')]
# # 循环这个列表
# # 显示 序号 用户要做的操作
# # 用户输入序号
# # 你通过序号找到对应的login或者register方法
# # 先实例化
# # 调用对应的方法，完成登录或者注册功能
# for i in range(len(lst)):
#     print(i, ':', lst[i][0])
# n = int(input())
# auth = Authentic('xiaoli', 18)
# if hasattr(auth, lst[n][1]):
#     getattr(auth, lst[n][1])()


# 作业2
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        pass
    def sleep(self):
        pass
# 用户输入名和密码
# 实例化对象
# 用户输入任意内容：
#   如果是属性名 打印属性值
#   方法  调用
#   什么都不是  什么都不做

