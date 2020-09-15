"""
启动文件
"""
# 绝对路径不好
# 动态获取blog路径，无论在谁的计算机中都可以找到这个文件
# import sys
# # 直接添加blog目录
# sys.path.append(r'D:\WorkSpace\Pycharm\fullstack\day18\blog')
# from core import src
# src.run()


# import sys
# import os
# # 直接添加blog目录
# print(__file__)  # 动态获取本文件的路径
# print(os.path.dirname(__file__))  # 父级目录
# print(os.path.dirname(os.path.dirname(__file__)))  # 爷爷级
# from core import src
# src.run()

import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from core import src

if __name__ == '__main__':
    src.run()
