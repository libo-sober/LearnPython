# 例1
# def func1():
#     print('in func1')
#     print(3)
#
#
# def func2():
#     print('in func2')
#     print(4)
#
#
# func1()
# print(1)
# func2()
# print(2)
# in func1
# 3
# 1
# in func2
# 4
# 2

# 例2
# def func1():
#     print('in func1')
#     print(3)
#
#
# def func2():
#     print('in func2')
#     func1()
#     print(4)
#
#
# print(1)
# func2()
# print(2)
# 1
# in func2
# in func1
# 3
# 4
# 2

# 例3
# def func2():
#     print(2)
#     def func3():
#         print(6)
#     print(4)
#     func3()
#     print(8)
#
#
# print(3)
# func2()
# print(5)
# 3
# 2
# 4
# 6
# 8
# 5

# 内置函数
# globals() locals()
a = 1
b = 2
def func():
    name = 'alex'
    age = 73
    print(globals())
    print(locals())  # 返回的是字典：字典里边是键值对，当前作用域的所有内容

print(globals())  # 返回的是自字典：字典里边是键值对，全局作用域的所有内容。
print(locals())