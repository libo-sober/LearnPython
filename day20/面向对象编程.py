"""
先来定义模子，用来描述一类事物
具有相同的属性和动作
"""
class Person(object):
    def __init__(self,name, sex, job, level, hp, weapon,ad):
        # 必须叫————init__这个名字，不能改变的，所有的在一个具体任务出现后拥有的属性
        # 都可以写在这里
        self.name = name
        self.sex = sex
        self.job = job
        self.level = level
        self.hp = hp
        self.weapon = weapon
        self.ad = ad
        # print('*' * 10)
    # print('in Person')
    # print('*' * 10)


alex = Person('alex','不详','搓澡工',0,250,'搓澡巾',1)  # alex就是对象 alex = Person()
# 的过程 是通过类获取一个对象的过程 ---> 实例化

print(alex, alex.__dict__)
# 类名()会自动的调用__init__方法
# 类是一个大的范围，是一个模子，它约束了事物有哪些属性
# 对象是类的产物

# dog类 实现狗的属性 名字 品种 血量 攻击力
class Dog(object):
    def __init__(self, name, kind, hp, ad):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.ad = ad

dog = Dog('Tom', '太低', 1000, 200)
print(dog, dog.__dict__)