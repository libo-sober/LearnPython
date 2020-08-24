# s1 = 'dsadasdasdasdasasd'
# # pyhton没有len()的话
# count = 0
# for i in s1:
#     count += 1
# print(count)
#
# count = 0
# l1 = [1, 2, 3, 4, 5, 6]
#
# for i in l1:
#     count += 1
# print(count)

# 代码重复太多
# 代码可读性差
# # 函数式编程
#
#
# def my_len(s):
#     count = 0
#     for i in s:
#         count += 1
#     print(count)
#
#
# s1 = 'dsadasdasdasdasasd'
# l1 = [1, 2, 3, 4, 5, 6]
#
# my_len(s1)
# my_len(l1)

# 函数：以功能（完成一件事）为导向，登录，注册，len。一个函数就是一个功能。随调随用
# 减少代码重复性，增强代码的可读性


# def meet():
#     print('打开探探')
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话')
#     print('约 ....  走起 ...')
# """
# 结构：def 关键字，定义函数。
#     meet 函数名：与变量设置相同，具有可描述性。
#     函数体：缩进。函数中尽量不要出现print。
# """
# # 函数什么时候执行？
# # 当遇到函数名加括号时执行。
# meet()

# 函数的返回值
# def meet():
#     print('打开探探')
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话')
#     print('约 ....  走起 ...')
#     # return '妹纸'
#     return '妹子', 123, [22, 33]
# return :在函数中遇到return直接结束函数。
# return：将数据返回给函数的执行者，调用者meet()。
# return饭hi多个元素是以元组的形式返回给函数的执行者。
# ret = meet()
# print(ret)
# print(type(meet()))  # <class 'tuple'>
"""
retuen 总结：
    1.在函数中，终止函数。
    2.return 可以给函数的执行者返回值。
        1）return 单个值   单个值
        2）return 多个值   (多个值，)
"""


# 函数的参数
# def meet(sex):  # 函数的定义：接受的参数是形式参数。
#     print('打开探探')
#     print('进行筛选：性别:%s' % sex)
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话')
#     print('约 ....  走起 ...')


# 函数的传参：让函数的封装的这个功能，盘活。
# 实参，形参。
# meet('男')
# meet('女')  # 函数的执行传的参数：实际参数。
# 函数的传参：实参，形参。
# 实参角度：
# 1.位置参数。从左到右一一对应。
# def meet(sex, age, skill, voice):  # 函数的定义：接受的参数是形式参数。
#     print('打开探探')
#     print('进行筛选：性别:%s，年龄：%s,python: %s, 声音：%s' % (sex, age, skill, voice))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话')
#     print('约 ....  走起 ...')
# meet('女', '18~40', 'python技术好的', '萝莉音')  # 函数的执行传的参数：实际参数。

# 写一个函数，只接受两个int的函数，函数的功能是将较大的数返回。
# def max_num(a, b):
#     # if a > b:
#     #     return a
#     # else:
#     #     return b
#     return a if a > b else b  # 三元运算符


# c = max_num(100, 1000)
# print(c)
# 2. 关键字参数
# 一一对应，顺序可以不打乱
# def meet(sex, age, skill, hight, weight):  # 函数的定义：接受的参数是形式参数。
#     print('打开探探')
#     print('进行筛选：性别:%s，年龄：%s,技术: %s, 身高：%s, 体重： %s' % (sex, age, skill, hight, weight))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话')
#     print('约 ....  走起 ...')
# meet('女', '25', 'python技术好的', 174, 130)  # 函数的执行传的参数：实际参数。
# meet(sex='女', age='25', weight=100, hight=174, skill='python技术好的')
# # 函数：传入两个字符串参数，将两个参数拼接完成后形成的结果返回
# def func(s1, s2):
#     return s1 + s2
# print(func(s1='Hello', s2='libo！'))
# 混合参数
# 位置参数一定要在关键字参数前边
# def meet(sex, age, skill, hight, weight):  # 函数的定义：接受的参数是形式参数。
#     print('打开探探')
#     print('进行筛选：性别:%s，年龄：%s,技术: %s, 身高：%s, 体重： %s' % (sex, age, skill, hight, weight))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话')
#     print('约 ....  走起 ...')
#     return '筛选结果：性别：%s, 体重： %s' % (sex, weight)
# # print(meet(25, weight=100, '女', hight=174, skill='python技术好的')) 位置参数未在关键字参数前边 报错
# print(meet('女', 25, weight=100, hight=174, skill='python技术好的'))
"""
实参角度：
    1.位置参数 按照顺序，一一对应
    2.关键字参数，一一对应
    3.混合参数：位置参数一定要在关键字参数的前边
"""
# 形参角度
# 1.位置参数 与实参角度的位置参数是一种
# 写一个函数，检测传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(l1):
#     # l2 = l1
#     # if len(l1) > 2:
#     #     l2 = l1[0:2]
#     # return l2
#     # return l1[0:2] if len(l1) > 2 else l1
#     return l1[0:2]
# print(func([1,2,3,4,5]))
# print(func([1,]))

# 默认参数
# 默认参数一定得在最后。
# 默认参数设置的意义：普遍经常用的。
# def meet(age, skill='python技术好的', sex='女'):  # 函数的定义：接受的参数是形式参数。
# #     print('打开探探')
# #     print('进行筛选：性别:%s，年龄：%s,技术: %s' % (sex, age, skill))
# #     print('左滑一下')
# #     print('右滑一下')
# #     print('找美女')
# #     print('悄悄话')
# #     print('约 ....  走起 ...')
# # # print(meet(25, 'pytohn技术好的'))
# # # print(meet(25,'pytohn技术好的', sex='男'))
# # print(meet(25,'运维技术好的', sex='男'))

# 形参角度：
# 1.位置参数
# 2.默认参数 经常用的参数
