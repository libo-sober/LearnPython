"""
pickle:
    将python中所有的数据类型，转换成字节串，序列化过程
    将字节串转换成python中数据类型，反序列化过程

"""

import pickle
#
# bys = pickle.dumps([1,2,3])
# print(type(bys))  # <class 'bytes'>
# print(bys)  # b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
#  保存了元组的数据类型
# bys = pickle.dumps((1,2,3))
# print(type(bys))  # v<class 'bytes'>
#
# res = pickle.loads(bys)
# print(type(res))  # <class 'tuple'>
# 所有的数据类型都可以字节化
# bys = pickle.dumps(set('abc'))
# res = pickle.loads(bys)
# print(type(res))  # <class 'set'>

# 把序列化的内容写进文件中
# with open('c.txt', mode='wb') as f:
#     pickle.dump([1,2,3], f)

# 从文件中反序列化pickle操作
# with open('c.txt', mode='rb') as f:
#     res = pickle.load(f)
#     print(type(res))  # <class 'list'>
#     print(res)  # [1, 2, 3]

# # 多次pickle数据到同一个文件中
# with open('c.txt', mode='wb') as f:
#     pickle.dump([1,2,3], f)
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)
#
# # 从文件中反序列化pickle操作
# with open('c.txt', mode='rb') as f:
#     for x in range(4):
#         res = pickle.load(f)
#         # print(type(res))  # <class 'list'>
#         print(res)  # [1, 2, 3]

# pickle常用的场景和json一样：一次性写入，一次性读取。

# json pickle 比较
"""
json:
1. 不是所有的数据类型都可以序列化，结果是字符串。
2. 不能多次对同一个文件序列化。
3. json数据可以跨语言。

pickle：
1. 所有的python数据类型都可以序列化，结果是字节串。
2. 可以多次对同一个文件序列化。
3. 不能跨语言。
"""


