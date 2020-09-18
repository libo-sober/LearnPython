"""
1. 作业
    定义一个圆形类，属性为半径


2. 计算器


"""
# sys.argv练习
# 写一个python脚本，在cmd里运行
# python xxx.py 用户户名 密码 cp 文件路径 目的地址
# python 作业讲解.py alex sb cp D:\WorkSpace\Pycharm\fullstack\day21\作业讲解.py D:\笔记
# python 作业讲解.py alex sb rm  D:\笔记\作业讲解.py
# python 作业讲解.py alex sb rm  D:\笔记\作业讲解.py D:\笔记\重命名.py
import sys
import os
import shutil
print(sys.argv)
if len(sys.argv) >= 5:
    if sys.argv[1] == 'alex' and sys.argv[2] == 'sb':
        if sys.argv[3] == 'cp':
            if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
                filename = os.path.basename(sys.argv[4])
                path = os.path.join(sys.argv[5], filename)
                shutil.copy2(sys.argv[4], path)
        elif sys.argv[3] == 'rm':
            if os.path.exists(sys.argv[4]):
                os.remove(sys.argv[4])
        elif sys.argv[3] == 'rename':
            if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
                os.rename(sys.argv[4], sys.argv[5])
else:
    print('您输入的命令无效')