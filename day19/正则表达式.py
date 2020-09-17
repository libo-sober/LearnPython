"""
1.re模块
3.待参数的装饰器\递归函数
"""
# ret = re.findall('9(\d)\d', '19740ash93010uru')
# print(ret)
# ret = re.findall('[a-z]', 'sal')
# print(ret)

# findall
# search


# # split
# # ret = re.split('\d+', 'alex222wusir')  # ['alex', 'wusir']
# # ret = re.split('(\d+)', 'alex222wusir')  # ['alex', '222', 'wusir']
# # print(ret)
# # # sub
# # ret = re.sub('\d+', 'H', 'alex123wusir456')  # alexHwusirH
# # print(ret)
# # # subn
# # ret = re.subn('\d+', 'H', 'alex123wusir456')  # ('alexHwusirH', 2)
# # print(ret)
# # match
# ret = re.match('\d+', '123taibai456')  # 从头开始找，规定这个字符串必须是什么样的
# ret = re.search('^\d+', '123taibai456')  # 作用相同 用来寻找这个字符串是不是满足含有条件的子内容
# print(ret)
# compile
# # 加入同一个正则表达式要被使用多次,节省了多次解析同一个正则表达式的时间
# ret = re.compile('\d+')
# ret1 = ret.findall('alex12343wusir')
# print(ret1)
# finditer  -- 节省空间


# 时间
# 你要完成一个带啊吗所需要执行的代码行数
# 你在执行代码的过程中底层程序是如何工作的
# 空间

# re模块的用法
# 分组命名
import re
re.findall()