"""
# 人狗大战
# 你是人  狗是一个npc
# 您一个回合 狗一个回合
# 狗掉的血是一个波动值
# 闪避概率
"""


class Person(object):
    def __init__(self, name, sex, job, level, blood, weapon, ad):
        # 必须叫————init__这个名字，不能改变的，所有的在一个具体任务出现后拥有的属性
        # 都可以写在这里
        self.name = name
        self.sex = sex
        self.job = job
        self.level = level
        self.blood = blood
        self.weapon = weapon
        self.ad = ad


class Dog(object):
    def __init__(self, name, kind, blood, ad, weapon):
        self.name = name
        self.kind = kind
        self.ad = ad
        self.blood = blood
        self.weapon = weapon

    def eat(self):
        print(f'{self.name}狗吃士')


person = Person('alex','不详','搓澡工',0,800,'搓澡巾',100)
dog = Dog('Tom', '太低', 1000, 200, '嘴')
count = 1
while person.blood > 0 and dog.blood > 0:
    print(f'第{count}回合')
    print(f"{person.name}用{person.weapon}攻击了{dog.name}...")
    dog.blood -= person.ad
    print(f"{dog.name}的血量为{dog.blood}")
    print(f"{dog.name}用{dog.weapon}攻击了{person.name}")
    person.blood -= dog.ad
    print(f"{person.name}的血量为{person.blood}")
    count += 1













