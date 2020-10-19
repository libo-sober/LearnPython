"""
测试自定义模块的导入
"""

# 自定义模块被其他模块导入时，其中的可执行语句会立即执行
# import a
# import time
# print(time.time())

# python中提供了一种可以判断自定义魔魁啊时属于开发阶段还是使用阶段.

# 使用自定义模块的成员
# print(a.a)
# a.f()

# 查看sys.path内容
import sys
# print(sys.path)

# 添加a.py所在的路径到sys.path中
# sys.path.append(r'D:\WorkSpace\Pycharm\fullstack\day12\aa')

# 使用相对路径找到aa文件
# print(__file__)  # 当前文件的绝对路径
# 使用os模块获取一个路径的父路径
import os
print(os.path.dirname(__file__) + '/aa')
sys.path.append(os.path.dirname((__file__)) + '/aa')
print(os.path.dirname(__file__))
import a

print(a.a)
