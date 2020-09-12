"""
time模块
三大对象：
    时间戳
    结构化时间对象（9大字段）
    字符串
"""

import time
# 如何获取时间戳
# 时间戳：从时间元年（1970/1/1 00：00：00）到现在经过的秒数。
# print(time.time())  1599875455.16338

# # 获取格式化时间对象：是9个字段组成的
# # 默认参数是当前系统时间的时间戳
# print(time.gmtime(1))  # 时间元年过一秒后对于的时间对象
# # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0,
# # tm_min=0, tm_sec=1, tm_wday=3, tm_yday=1, tm_isdst=0)
# print(time.gmtime())  # GMT:格林尼治时间
# # time.struct_time(tm_year=2020, tm_mon=9, tm_mday=12,
# # tm_hour=2, tm_min=2, tm_sec=7, tm_wday=5, tm_yday=256, tm_isdst=0)
# print(time.localtime())  # 当地时间
# # time.struct_time(tm_year=2020, tm_mon=9, tm_mday=12, tm_hour=10,
# # tm_min=5, tm_sec=48, tm_wday=5, tm_yday=256, tm_isdst=0)

# # 格式化时间对象和字符串之间的转换
# s = time.strftime("year:%Y %m %d %H:%M:%S")
# print(s)

# # 把一个时间字符串转换成一个时间对象
# time_obj = time.strptime("2010 10 10", "%Y %m %d")
# print(time_obj)
# # time.struct_time(tm_year=2010, tm_mon=10, tm_mday=10, tm_hour=0,
# # tm_min=0, tm_sec=0, tm_wday=6, tm_yday=283, tm_isdst=-1)

# # 时间对象-->时间戳
# t1 = time.localtime()  # 时间对象
# t2 = time.mktime(t1)  # 获取对应的时间戳
# print(t2)
# print(time.mktime(time.localtime()))

# 暂停当前程序，睡眠xxx秒
# time.sleep(xxx)
for x in range(5):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    # 休眠一秒钟
    time.sleep(1)

