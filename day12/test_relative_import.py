"""
测试相对导入
"""
import os,sys

# 把项目所在的父路径加到sys.pass中
sys.path.append(os.path.dirname(__file__) + '/xx')

from xx.y import yy
print(yy.age2)
yy.f2()

# 怎么调用zz的成员？
# print(yy.zz.age)
# # yy.zz.f()

print(yy.age2)
yy.f()
