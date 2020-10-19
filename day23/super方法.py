class A:
    def func(self):
        print('A')


class B(A):
    def func(self):
        super().func()
        print('B')


class C(A):
    def func(self):
        super().func()
        print('C')


class D(B, C):
    def func(self):
        super().func()  # super是按照mro顺序来寻找当前类的下一个类的
        print('D')


D().func()
# A
# B
# C
# super是按照mro顺序来寻找当前类的下一个类的
# 在python3中不需要传参，在py2的新式类中，需要传参
# 在py2的经典类中（不继承object）不支持使用super()

# 在单继承中执行父类的同名方法
# super().__init__(name) 父类的init方法
