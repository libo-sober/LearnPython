# 普通类
# 抽象类
#   是一个开发的规范 约束它的所有子类必须遵守的规则
# 支付程序
#     微信支付  url链接,告诉你们参数什么格式
#     支付宝支付
# class Payment:  # 抽象类
#
#     def pay(self, money):
#         raise NotImplementedError('请在子类中重写pay函数')
#
#
#
#
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
#     def daspay(self, money):
#         dic = {'uname': '用户名', 'price': money}
#         # 想办法调用支付宝支付吧dic纯过去
#         print(f'{self.name}通微信支付{money}成功')
#
# # ali = Alipay('小明')
# # ali.pay(300)
#
# # 归一化设计
# def pay(name, price, way):
#     if way == 'WeChat':
#         obj = WeChat(name)
#         obj.pay(price)
#     elif way == 'Alipay':
#         obj = Alipay(name)
#         obj.pay(price)
#
#
# # pay('alex', 400, 'Alipay')
# pay('alex', 400, 'WeChat')

# 实在抽象类的另一种方式:约束力强,但是以来ABC模块
from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):  # 抽象类
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError('请在子类中重写pay函数')




class Alipay(Payment):
    def __init__(self, name):
        self.name = name
    def pay(self, money):
        dic = {'uname':'用户名','price':money}
        # 想办法调用支付宝支付吧dic纯过去
        print(f'{self.name}通过支付宝支付{money}成功')

class WeChat(Payment):
    def __init__(self, name):
        self.name = name

    # def daspay(self, money):
    #     dic = {'uname': '用户名', 'price': money}
    #     # 想办法调用支付宝支付吧dic纯过去
    #     print(f'{self.name}通微信支付{money}成功')

# ali = Alipay('小明')
# ali.pay(300)


def pay(name, price, way):
    if way == 'WeChat':
        obj = WeChat(name)
        obj.pay(price)
    elif way == 'Alipay':
        obj = Alipay(name)
        obj.pay(price)


# pay('alex', 400, 'Alipay')
pay('alex', 400, 'WeChat')



