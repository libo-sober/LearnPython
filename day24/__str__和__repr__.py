# __new__
# class A:
#     def __new__(cls, *args, **kwargs):  # 构造方法
#         o = super().__new__(cls)
#         print('执行new', o)
#         return o
#     def __init__(self):
#         print('执行init', self)
#
# A()

# 实例化的时候
# 先创建一块空间，有一个指针能指向类 --> __new__来完成的
# 再调用init --> __init__

# 设计模式 -- 单例模式
# 一个类 从头到尾 只会创建一次self空间
# class Baby:  # 面试用
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#     def __init__(self, cloth, pants):
#         self.cloth = cloth
#         self.pants = pants
# b1 = Baby('红毛衣', '绿皮库')
# print(b1.cloth)
# b2 = Baby('白衬衫', '黑豹问')
# print(b1.cloth)
# print(b2.cloth)
from 单例 import baby
# from 单例 import baby 其他文件导入 都是同一个baby内存地址
print(baby.cloth)

# __str__
class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period
    def __repr__(self):
        return 'aaaaa'
    def __str__(self):
        return ','.join([self.name,str(self.price),self.period])
python = Course('python', 21800, '6 month')
linux = Course('linux', 19800, '5 month')
mysql = Course('mysql', 21800, '6 month')
go = Course('go', 21800, '6 month')
print(repr(go))
# print(go)
lst = [python, linux, mysql, go]
# 打印对象时， __str__返回的什么，就打印什么。
# 在%s拼接时， str(对象)时，都会调用__str__
# 如果找不到__str__就调用__repr__
# 当遇到用%r进行字符串拼接时，或者用repr(对象)时， 只调用__repr__
for course in lst:
    print(course)
# for index, c in enumerate(lst, 1):
#     print(index, c.name, c.price, c.period)
# num = int(input('>>>'))
# course = lst[num-1]
# print(f'恭喜您选择的课程为{course.name} 价格{course.price}元')










