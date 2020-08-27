# 用一行代码去构建一个比较复杂有规律的列表。
# l1 = []
# for i in range(1, 101):
#     l1.append(i)
# print(l1)
# # 这就是列表推导式
# l2 = [i for i in range(1, 101)]
# print(l2)
# 循环模式
# 将10以内所有整数的平方写入列表。
# l3 = [i ** 2 for i in range(1, 10)]
# print(l3)
# # 将10以内所有的偶数写入列表
# l4 = [i for i in range(1, 101) if i % 2 == 0]
# print(l4)
# print([i for i in range(2, 101, 2)])
# # 从python1期到python100期写入列表lst
# lst = [f'python{i}期' for i in range(1, 101)]
# print(lst)
# # 筛选模式
# # 30以内能被3整除的数
# print([i for i in range(1, 31) if i % 3 == 0])
# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# l1 = ['barry', 'alex', 'ab', 'wusir', 'xo']
# l2 = [i.upper() for i in l1 if len(i) > 3]
# print(l2)
# # 含有两个'e'的所有的人名留下来，并大写
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'wendy', 'Jennifer', 'Sherry', 'Eva']]
# l3 = []
# for i in names:
#     for name in i:
#         if name.count('e') == 2:
#             l3.append(name.upper())
#
# print(l3)
# # 一行代码
# # 多层循环的列表推导式
# print([name.upper() for i in names for name in i if name.count('e') == 2])
#
# # 生成器表达式：
# # 与列表推导式的写法几乎一模一样,也有筛选模式，循环模式，多层循环模式，写法上只有一个不同
# # 把 [] 改成 ()
# print([i for i in range(1, 11)])
# print((i for i in range(1, 11)))  # 生成器
# obj = (i for i in range(1, 11))
# print(next(obj))
# print(next(obj))
#
#
# # 总结
# # 列表推导式：
# #   缺点：
# #   1. 有毒。列表推导式只能构建比较复杂并且有规律的列表。不要太着迷。
# #   2. 超过三层循环才能构建成功的，就不建议用列表推导式。
# #   3. 查找错误（debug模式）不行。
# #   优点：
# #   1. 一行构建，简单。
# #   2. 装逼。
#
# # 构建一个列表：[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
# list4 = [i for i in range(2, 11)] + list('JQKA')
# print(list4)

# 列表推导式与生成器表达式的区别:
# 写法上： [] ()
# iterable iterator

# 字典推导式(了解)
# list1 = ['jay', 'jj', 'meet']
# list2 = ['周杰伦', '林俊杰', '元宝']
# dic = {list2[i]: list1[i] for i in range(len(list1))}
# print(dic)
# # 集合推导式
# print({i for i in range(1, 11)})  # 集合是无序的


