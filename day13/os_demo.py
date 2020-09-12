"""
os:和操作系统相关的操作被封装到这个模块中。
"""
import os
# 和文件操作相关：重命名，删除...
# 删除
# os.remove(r'a')

# 重命名
# os.rename('a.txt', 'aa/b.txt')  # 不影响里面的内容

# # 删目录：必须是空目录,不会放在回收站里
# os.removedirs(r'aa')  # OSError: [WinError 145] 目录不是空的。: 'aa'

# # 如果不是空的想删除的话：
# # 1. 先删最里面的，再删外层的。
# # 2. 使用shutil模块可以删除带内容的目录
# import shutil
# shutil.rmtree(r'aa')

# 和路径相关的操作，被封装到另一个子模块中：os.path
# # 获取目录名
# res = os.path.dirname(r'd:/aaa/bbb/ccc/a.txt')  # 不判断路径是否存在。
# print(res)  # d:/aaa/bbb/ccc
#
# # 获取文件名
# res = os.path.basename(r'd:/aaa/bbb/ccc/a.txt')  # 不判断路径是否存在。
# print(res)  # a.txt
# # 把路径中的路径名和文件名且分开，结果是元组
# res = os.path.split(r'd:/aaa/bbb/ccc/a.txt')
# print(res)  # ('d:/aaa/bbb/ccc', 'a.txt')
#
# # # 拼接路径
# path = os.path.join('d:\\', 'aaa', 'bbb', 'ccc', 'a.txt')
# print(path)  # d:\aaa\bbb\ccc\a.txt
# # 如果是/开头的路径，默认是在当前盘符下 r'a/b/c'
# res = os.path.abspath(r'd:\aaa\bbb\ccc\a.txt')
# print(res)

# # 判断
# print(os.path.isabs(r'd:/a.txt'))  # True
# print(os.path.isdir(r'd:/aaa.txt'))  # True  不能只看后缀名，文件不存在的话为False
# print(os.path.exists(r'd:/aaa.txt'))  # True
# print(os.path.isfile(r'd:/aaa.txt'))  # False 不是文件或者文件不存在






