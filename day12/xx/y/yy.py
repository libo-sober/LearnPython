"""
此模块作为对外引用的入口
"""
# 相对导入同项目下的模块
# from ..z import zz    # 容易象外界暴露zz模块
from ..z.zz import *

# 不使用相对导入的方式，导入本项目中的模块
# 通过当前文件的路径找到你想导入的z的路径
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + '/z')
from zz import *

# 定义自己的成员
age2 = 88
def f2():
    print('f2')


