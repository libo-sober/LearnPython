# 三大特性”封装继承和堕胎
# 猫
    # 吃 喝 睡
    # 爬树
# 狗
    # 吃 喝 睡
    # 看家
# class Cat(object):
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print(f'{self.name}吃')
#     def drunk(self):
#         print(f'{self.name}喝')
#     def sleep(self):
#         print(f'{self.name}睡')
#     def pashu(self):
#         print(f'{self.name}会爬树')
# #
# class Dog(object):
#     def __init__(self, namw):
#         self.name = namw
#     def eat(self):
#         print(f'{self.name}吃')
#     def drunk(self):
#         print(f'{self.name}喝')
#     def sleep(self):
#         print(f'{self.name}睡')
#     def kanjia(self):
#         print(f'{self.name}会看家')
#
# bai = Cat('小白')
# hei = Dog('小黑')
# bai.eat()
# bai.pashu()
# hei.drunk()
# hei.kanjia()

# 继承---需要解决代码的重复
# class A:
#     pass
# class B(A):
#     pass
# B继承A，A是父类，B是子类
# A是父类  基类 超类
# B是子类 派生类
# 子类可以使用父类中的：方法 静态变量
# 子类与父类的方法重名时只调用子类的方法
# 子类想要调用弗雷的方法同时还想执行自己的同名方法
# 父类名.方法名(self)
# class Animal(object):
#         def __init__(self, name, food):
#             self.name = name
#             self.food = food
#             self.blood = 100
#             self.wise = 100
#
#         def eat(self):
#             print(f'{self.name} eat {self.food}')
#
#         def drunk(self):
#             print(f'{self.name}喝')
#
#         def sleep(self):
#             print(f'{self.name}睡')
#
#
# class Cat(Animal):
#     def eat(self):  # 方法的重载
#         self.blood += 1
#         Animal.eat(self)
#     def pashu(self):
#         print(f'{self.name}会爬树')
#
#
# class Dog(Animal):
#     def eat(self):  # 方法的重载
#         self.wise += 19
#     def kanjia(self):
#         print(f'{self.name}会看家')

# cat = Cat('小白', '猫粮')
# cat.eat()
# # cat.pashu()
# dog = Dog('小黑', '狗粮')
# # dog.kanjia()
# # dog.sleep()
# dog.eat()
#  先开辟空间，空间里有一个类指针，只想Cat
# 调用init，对象在自己的空间中找init没找到，到Cat类中找init也没找到
# 找弗父类中的init

# 父类和子类方法的选择：
# 子类的对象，如果去调用方法
# 永远优先调用自己的 自己没有用父类的
# 如果自己有还想用父类的，则父类名.方法名(self)
# class Foo:
#     def __init__(self):
#         self.func()  # 在每一个self调用func时候的，我们不看这句话实在哪里执行，只看self是谁
#     def func(self):
#         print('in Foo')
# class Son(Foo):
#     def func(self):
#         print('in Son')
# Son()
#
# # 如何给狗和猫定制个性化属性
# 猫：眼睛的颜色
# 狗：型号
class Animal(object):
    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.blood = 100
        self.wise = 100

    def eat(self):
        print(f'{self.name} eat {self.food}')

    def drunk(self):
        print(f'{self.name}喝')

    def sleep(self):
        print(f'{self.name}睡')


class Cat(Animal):
    def __init__(self,name, food, eye_color):
        Animal.__init__(self, name, food)  # 调用父类的初始化，去完成一些通用属性的初始化
        self.eye_color = eye_color
    def eat(self):  # 方法的重载
        self.blood += 1
        Animal.eat(self)

    def pashu(self):
        print(f'{self.name}会爬树')


class Dog(Animal):
    def eat(self):  # 方法的重载
        self.wise += 19

    def kanjia(self):
        print(f'{self.name}会看家')

cat = Cat('小白', '猫粮', '蓝色')

# 多继承,有好几个参
# 有一些语言时不支持多继承的
# python可以在面向对象中支持多继承
# class A:
#     def func(self):
#         print('in A')
# class B:
#     def func(self):
#         print('in   B')
# class C(B,A):  # 谁写在前边先找谁
#     # def func(self):
#     #     print('in C')
#     pass
#
# c = C()
# c.func()
print(isinstance(cat, Animal))  # True 判断一个对象是不是它的

# 类名调用是函数
# 对象调用是方法



