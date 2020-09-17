"""
面向对象：
    初识面向对象
        一种新的编程思路
        一些概念
        一些语法
"""
# 游戏公司
# 人狗大战
# 人：血条 武器 名字 性别 职业 攻击力
#   技能:搓澡
# 狗：名字 种类 血条
#   技能

alex = {
    'name':'alex',
    'sex':'不详',
    'job':'搓澡工',
    'level':0,
    'hp':250,
    'weapon':'搓澡巾',
    'ad':1,
}

小白 = {
    'name':'小白',
    'kind':'泰迪',
    'hp':5000,
    'ad':249,
}

# 1.你怎么保证所有的玩家一初始化时都拥有相同的属性
# 2.每来一个新的玩家，我们都自己手动的创建一个字典，然后想字典中传值，这样好不好？
# 3.人物和狗的技能怎么安排？

# def Person(name, sex, job, hp, weapon, ad, level=0):
#     dic = {
#         'name': name,
#         'sex': sex,
#         'job': job,
#         'level': level,
#         'hp': hp,
#         'weapon': weapon,
#         'ad': ad,
#     }
#   return dic
#
# alex = Person('alex',不详','搓澡工',)

print(小白)







