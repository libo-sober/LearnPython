# property
from math import pi
class Circle:
    def __init__(self, r):
        self.r = r
    # 用property把一个方法装饰成一个属性， 在调用时不要加()，可以直接得到返回值
    @property
    def area(self):
        return self.r ** 2 * pi

import time
c1 = Circle(5)
print(c1.area)  # 装饰后的属性
# 变量的属性和方法？
# 半径 和 面积    --- 属性
# 登录  注册  ----- 方法

class Person:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
    @property
    def age(self):  # 装饰的方法不能有参数
        return time.localtime().tm_year - self.birth

wang = Person('老王', 1997)
print(wang.age)
# property的第二个场景
class User:
    def __init__(self,user,pwd):
        self.user = user
        self.__pwd = pwd
    @property
    def pwd(self):  # 不能改
        return self.__pwd
alex = User('Alex', 'sbsbsb')
print(alex.pwd)

# property进阶
class Goods:
    discount = 0.8
    def __init__(self, name, origin_price):
        self.name = name
        self.__price = origin_price
    @property
    def price(self):
        return self.__price * self.discount
    @price.setter
    def price(self, new_price):  # 必须按要求改
        if isinstance(new_price, int):
            self.__price = new_price
    @price.deleter
    def price(self):
        del self.__price

apple = Goods('苹果', 5)
# print(apple.price) # 调用的是被@property装饰的price
apple.price = 10  # 调用的是被@price.setter装饰的price
print(apple.price)
# del apple.price

