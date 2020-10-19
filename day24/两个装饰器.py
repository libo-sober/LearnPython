# 两个装饰器
    # @classmethod
    # @ staticmethod
# 一些内置的魔术方法
    # __new__
    # __call__
    # __len__
    # __eq__
    # __str__
    # __repr__

# classmethod
class Goods:
    __discount = 0.8
    def __init__(self):
        self.__price = 5
        self.price = self.__price * self.__discount
    # 定义了一个方法，默认传self，但是没有用
    # def set_discount(self, new_discount):
    @classmethod  # 把一个对象绑定的方法，修改成一个类方法
    def set_discount(cls, new_discount):
        # Goods.__discount = new_discount
        # classmethog 用cls和goods都可以，但是减一用cls,因为类名会改变
        cls.__discount = new_discount
# 调用类方法时可以不用实例化
# 在方法中仍然可以引用类中的静态变量
# 什么时候用？
# 定义了一个方法，默认传self，但是没有用
# 你在这个方法中用到了当前类名
Goods.set_discount(0.6)  # 类方法可以通过类名调用，也可以通过对象名调用
apple = Goods()
print(apple.price)
# # 修改折扣0.6
# apple.set_discount(0.6)
#
# apple2 = Goods()
# print(apple2.price)
import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        time_str = time.localtime()
        y = time_str.tm_year
        m = time_str.tm_mon
        d = time_str.tm_mday
        return cls(y, m, d)

date = Date.today()
print(date.year, date.month, date.day)

# @staticmethod 被装饰的方法会成为一个静态方法
# def login():
#     print('login')
class User:
    @staticmethod
    # 本身是一个普通的函数，被挪到类的内部执行，那么直接给这个函数添加@staticmethod装饰器
    def login():
        print('login')
        # 在函数内部既不会用来self，也不会用到cls

User.login()

