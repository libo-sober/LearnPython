"""
序列化
"""

# json:将数据转换成字符串，用于存储或网络传输。
# 只能写字符串
# with open('a.txt', mode='wt', encoding='utf-8') as f:
#     f.write(10)
# TypeError: write() argument must be str, not int

# t -> text
# b -> binary
# a -> append
# w -> write
# r -> read
# 默认是rt

import json
# s = json.dumps([1,2,3])  # 把指定的对象转换成json格式的字符串
# print(type(s))  # <class 'str'>
# print(s)  # '[1, 2, 3]'

# s = json.dumps((1,2,3))  # 元组序列化后就变成列表了
# print(s)  # '[1, 2, 3]'

# res = json.dumps(10)
# print(res)  # '10'

# res = json.dumps({'name': 'Andy', 'age': 10})
# print(res)  # '{"name": "Andy", "age": 10}'

# 集合不能序列化
# res = json.dumps({1,2,3})  # TypeError: Object of type 'set' is not JSON serializable
# print(res)

# # 将json结果写进文件中
# with open('a.txt', mode='at', encoding='utf-8') as f:
#     json.dump([1,2,3], f)

# 反序列化
# res = json.dumps([1,2,3])
# lst = json.loads(res)  # 反序列化
# print(type(lst))  # <class 'list'>
# # s = '[1,2,3]'

# 元组会变成列表
# res = json.dumps((1,2,3))
# lst = json.loads(res)  # 反序列化
# print(type(lst))  # <class 'list'>

# 从文件中反序列化
# with open('a.txt', encoding='utf-8') as f:
#     res = json.load(f)
#     print(type(res))  # <class 'list'>
#     print(res)  # '[1, 2, 3]'


# json
# json.dumps(obj
# json.dump(obj,fp)
# json.loads(s)
# json.load(f)

# json文件通常是一次性写，一次性读。
# 使用另一种方式可以实现多次写多次读。
# 把需要序列化的对象通过多次序列化的方式，用文件的write方法把多次序列化后的json字符串写道文件中。
# with open('b.txt', mode='at', encoding='utf-8') as f:
#     f.write(json.dumps([1,2,3]) + '\n')
#     f.write(json.dumps([4, 5, 6]) + '\n')

# # 把分次序列化的json字符串，反序列化回来
with open('b.txt', mode='rt', encoding='utf-8') as f:
    # res = json.loads(f.readline().strip())
    # print(res)
    # res2 = json.loads(f.readline().strip())
    # print(res2)
    #
    for x in f:
        print(json.loads(x.strip()))

