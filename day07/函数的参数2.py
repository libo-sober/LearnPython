# 形参角度，
# 万能参数。
# # 第一期
# def eat(a,b,c,d):
#     print("我请你吃：%s,%s,%s,%s。" % (a,b,c,d))
#
#
# eat('蒸羊羔', '蒸熊掌', '烧花鸭', '烤乳猪')
# 第二期
# def eat(a,b,c,d,e,f):
#     print("我请你吃：%s,%s,%s,%s,%s,%s。" % (a,b,c,d,e,f))
#
#
# eat('蒸羊羔', '蒸熊掌', '烧花鸭', '烤乳猪','烧子鹅', '烧雏鸡')

# 急需要一种形参，可以接收所以的形参。万能参数。
# 万能参数：*args，约定熟成：args。
# * 函数定义时， * 代表聚合。它将所有的位置参数聚合成一个元组赋值给args。
# def eat(*args):
#     print(args)  # 列表
#     print("我请你吃：%s,%s,%s,%s,%s,%s。" % args)
#
#
# eat('蒸羊羔', '蒸熊掌', '烧花鸭', '烤乳猪','烧子鹅', '烧雏鸡')
# # 写一个函数，计算你传入函数的所有数字的和
# def sum_num(*args):
#     # i = 0
#     # for num in args:
#     #     i += num
#     # return i
#     return sum(args)
# print(sum_num(1,2,3,4,5,6))
# **kwargs
# 函数定义时： ** 将所有的关键字参数聚合到一个字典中，将这个字典赋值给了kwargs。
# def func(**kwargs):
#     print(kwargs)
# func(name='alex', age=73, sex='laddyboy') {'name': 'alex', 'age': 73, 'sex': 'laddyboy'}
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# func('23', 'dasd', 12, name='年后', sex='女')
# 形参角度的参数的顺序
# **args放在所有位置参数的后边且在所有默认参数前边，**kwargs放在所有默认参数后边
# def func(a, b, *args, name='libo',sex='男', **kwargs):
#     print(a,b)
#     print(args)
#     print(sex)
#     print(name)
#     print(kwargs)
# func(1,2,3,4,5,6,sex='女',name='alex',age=80,love='paly')
# 1 2
# (3, 4, 5, 6)
# 女
# alex
# {'age': 80, 'love': 'paly'}
# 形参角度的第四个参数：仅限关键字参数
# 这里的make其实为默认参数，传值的时候必须键入关键字，不给传值会报错，所以必须传值。
# def func(a, b, *args, name='libo',make,sex='男', **kwargs):
#     print(a,b)
#     print(args)
#     print(sex)
#     print(name)
#     print(make)
#     print(kwargs)
# func(1,2,3,4,5,6,make='niaho',sex='女',name='alex',age=80,love='paly')
# 形参角度最终的次序：位置参数，*args，默认参数，仅限关键字参数，**kwargs
# * ** 在函数的调用时，* 代表打散。
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# func([1,2,3],[4,5,6]) ([1, 2, 3], [4, 5, 6])
# # func(*[1,2,3],*[4,5,6]) (1, 2, 3, 4, 5, 6)
# func({'name':'小明','age':19},{'love':'play','make':'sex'})
# ({'name': '小明', 'age': 19}, {'love': 'play', 'make': 'sex'})
# {}
# func(**{'name':'小明','age':19},**{'love':'play','make':'sex'})
# ()
# {'name': '小明', 'age': 19, 'love': 'play', 'make': 'sex'}
# print(*[[1,2,3],[4,5,6]])
# print(*[1,2,3])
# 二维数组的输出方式
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(arr)):
#     print(*arr[i])
# 1 2 3
# 4 5 6
# 7 8 9
