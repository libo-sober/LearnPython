"""
sys模块:和python解释器相关的操作
"""
# 获取命令行方式运行的脚本后面的参数
import sys
# print('脚本名:', sys.argv[0])  # 脚本名
# print('第一个参数：', sys.argv[1])  # 第一个参数
# print('第二个参数：', sys.argv[2])  # 第二个参数

# print(type(sys.argv[1]))  # str
#
# arg1 = int(sys.argv[1])
# arg2 = int(sys.argv[2])
# print(arg1 + arg2)
# 解释器取寻找模块的路径
# sys.path

# 已经加载的模块
print(sys.modules)
# import datetime
# datetime.time()

