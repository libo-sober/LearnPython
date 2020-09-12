"""
datetime:日期时间模块

封装了一些和日期时间相关的类

date
time
datetime
timedelta
"""
import datetime
# # date类：
# d = datetime.date(2010, 10, 10)
# print(d)  # 2010-10-10
# # 获取date对象的各个属性
# print(d.year, d.month, d.day)  # 2010 10 10
#
#
# # time类：
# t = datetime.time(10, 48, 59)
# print(t)  # 10:48:59
# print(t.hour, t.minute, t.second)  # 10 48 59
#
#
# # datetime
# dt = datetime.datetime(2010, 11, 11, 11, 11, 11)
# print(dt)  # 2010-11-11 11:11:11

# # datetime中的类，主要是用于数学计算的。
# # timedelta:时间变化量。
# # class datetime.timedelta(days=0, seconds=0, microseconds=0,
# # milliseconds=0, minutes=0, hours=0, weeks=0)
# td = datetime.timedelta(days=1)
# print(td)  # 1 day, 0:00:00
# # 参与数学运算
# # 创建时间对象
# # date, datetime, timedelta 不能和time对象进行运算
# d = datetime.datetime(2010, 10, 10)
# res = d + td
# print(res)  # 2010-10-11 00:00:00

# # 时间变化量的计算是否会产生进位?会的。
# t = datetime.datetime(2010, 10, 10, 10, 10, 59)
# td = datetime.timedelta(seconds=3)
# res = t + td
# print(res)  # 2010-10-10 10:11:02

# # 练习：计算某一年的二月份有多少天？
# # 普通的算法：根据年份计算是否是闰年，是。29天，否，28天。
# # 用datetime模块
# # 首先创建出指定年份的3月1号，然后让它往前再走一天。
# year = int(input('输入年份：'))
# # 创建指定年份的date对象
# d = datetime.date(year, 3, 1)
# # 创建一天的时间段
# td = datetime.timedelta(days=1)
# res = d - td
# print(res.day)

# 和是时间段进行运算的结果 类型？？？与另一个操作数保持一致。如果没有秒则不显示不会报错。
d = datetime.date(2010, 10, 10)  # 与这个类型保持一致
td = datetime.timedelta(days=1)
res = d - td
print(type(res))  # <class 'datetime.date'>
