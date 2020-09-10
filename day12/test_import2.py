"""
导入模块的多种方式：

"""
# 把自定义模块的路径田间道sys.path中
import os,sys
sys.path.append(os.path.dirname(__file__) + '/aa')

# 使用from ... import xxx 导入方式
# 容易产生命名冲突
# from my_modul import age
#
# print(age)

# 使用import xxx 导入
# import my_modul
# print(my_modul.age)

# 使用别名避免命名冲突
# from my_modul import age as a
# age = 100
# print(age, a)

# 给模块起别名
# import my_modul as m
# print(m.age)
# m.f1()

# 验证__all__控制的成员
# from my_modul import *
# print(age)
# print(age2)
# print(age3)  # NameError: name 'age3' is not defined

# 使用如下方式可以绕过__all__方式
import my_modul as m
print(m.age)
print(m.age2)
print(m.age3)
