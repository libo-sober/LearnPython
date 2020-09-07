# # id 身份证号
# i = 100
# s = 'alex'
# print(id(i))  # 1854044272
# print(id(s))  # 2392423437904
#
# # == 比较的是两边的值
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# print(l1 == l2)  # True
# s1 = 'alex'
# s2 = 'alex '
# print(s1 == s2)  # False
#
# # is 判断的是内存地址是否相同
# l3 = [1, 2, 3]
# l4 = [1, 2, 3]
# print(l3 is l4)  # False
# s3 = 'alex'
# s4 = 'alex'
# print(id(s3))  # 2663093999184
# print(id(s4))  # 2663093999184
# print(s3 is s4)  # True
# # id相同，它的值一定相同
# # 值相同，id不一定相同
#
#
# # 代码块
# # 我们所有的代码都需要以来代码块执行
# # 一个文件就创建一个代码块
# # 交互式命令下一行就是一个代码块
# tu1 = (1, 2, 3)
# tu2 = (1, 2, 3)
# print(id(tu1), id(tu2))  # 元组不行

# 集合
# 集合的创建
# # set1 = set({1, 3, "barry", False})
# set1 = {1, 3, '太白金星', 4, 'alex', False, '武大'}
# print(set1)  # {False, 'alex', 1, 3, 4, '武大', '太白金星'}
#
# # 空集合
# print(type({}))  # 空字典
# print(type(set()))  # 空集合
# 集合的有效性测试
# set2 = {'太白金星', '潘金莲', 'alex', '武大郎', '武松'}
# print(set2)  # {'alex', '武大郎', '武松', '潘金莲', '太白金星'}
# # add 增加
# set2.add('西门庆')
# print(set2)  # {'alex', '武大郎', '西门庆', '武松', '潘金莲', '太白金星'}
#
# # update 迭代着增加  把每个元素增加进去 而且去重
# set2.update('李逵李逵')
# print(set2)  # {'alex', '武大郎', '逵', '西门庆', '武松', '潘金莲', '李', '太白金星'}
#
# # remove 删除 按元素删除
# set2.remove('太白金星')
# print(set2)  # {'逵', '李', '潘金莲', '西门庆', '武松', '武大郎', 'alex'}
#
# # pop 随机删除
# set2.pop()
# print(set2)  # {'alex', '武大郎', '西门庆', '李', '潘金莲', '逵'}
#
# # 变相改值
# set2.remove('alex')
# set2.add('libo')
# print(set2)  # {'libo', '武松', '李', '潘金莲', '逵', '武大郎'}

# # 交集  & 或者 intersection
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1 & set2)
# print(set1.intersection(set2))  # {4, 5}
#
# # 并集  | 或则 union
# print(set1 | set2)
# print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8}
#
# # 差集 - 或者 difference
# print(set1.difference(set2))
# print(set1 - set2)  # {1, 2, 3}
# print(set2.difference(set1))
# print(set2 - set1)  # {8, 6, 7}
#
# # 反交集(先取并集，然后再减去交集) ^ 或者 symmetric_difference
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}

# # 子集
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5, 6, 7, 8}
#
# print(set1 < set2)  # True
#
# # 超集
# print(set2 > set1)

# 列表去重 并不保持原来的顺序
l1 = [1, 1, 1, 2, 2, 2, 3, 4, 4, 5]
set1 = set(l1)
l1 = list(set1)
print(l1)

# 用处： 数据之间的关系，列表去重。


