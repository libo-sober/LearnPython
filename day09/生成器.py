# 函数
# def func():
#     print(11)
#     print(22)
#     return 3
#
#
# ret = func()
# print(ret)
# 生成器函数
# def func():
#     print(11)
#     print(22)
#     yield 3  # 后边写一个next函数就执行到这里，再写一个就接着执行到下一个yeild
#     a = 1
#     b = 2
#     c = a + b
#     print(c)
#     yield 4
# func()  # 不执行
# print(func)
# ret = func()
# print(ret)  # <generator object func at 0x000001E6D1DB9780>
# print(next(ret))  # 一次返回一个yield值
# print(next(ret))
# 一个next对应一个yield

# return 和 yeild 有什么区别
# return：函数中只存在一个return结束函数，并且给函数的执行者饭hi之。
# yeild：只要函数中有yield那么它就是生成器函数而不是函数了。
# 生成器函数中可以存在多个yield，yield不会结束生成器函数，一个yield对应一个next()，

# 吃包子
# 这种一下九八2000个包子存进内存
# def func():
#     l1 = []
#     for i in range(1, 5001):
#         l1.append(f'{i}号包子')
#     return l1
# ret = func()
# print(ret)
# def gen_func():
#     for i in range(1, 5001):
#         yield f'{i}号包子'
#
# ret = gen_func()
# # next一次产生一个 极大节省内存
# # 只产生一个数据集里边只有一个包子，这个被拿走下一个放进去。
# # 需要200个包子
# for i in range(200):
#     print(next(ret))
# # 再要200个包子 从201开始
# for i in range(200):
#     print(next(ret))


# yield from  将l1这个列表变成了迭代器返回
# def func():
#     l1 = [1,2,3,4,5]
#     yield from l1  # 将l1这个列表变成了迭代器返回
#     """
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     """
# ret = func()
# print(next(ret))  # 得到列表的第一个值
# print(next(ret))
# print(next(ret))
# print(next(ret))
# print(next(ret))

# def func():
#     list1 = ['都是', '打散', '的撒', '离开']
#     list2 = ['空', '发帖人', '解耦i', '同意']
#     yield from list1
#     yield from list2
#
# g = func()
# for i in range(8):
#     print(next(g))
# # for i in g:
# #     print(i)

