# # python提供了68个内置函数。
# # 今天将的这部分了解即可
# # eval() 剥去字符串的外衣运算里面的代码,有返回值的。
# s1 = '1 + 3'
# print(s1)  # '1 + 3'
# print(eval(s1))  # 4
# s = '{"name": "alex"}'
# print(s, type(s))  # {"name": "alex"} <class 'str'>
# print(eval(s), type(eval(s))) # {'name': 'alex'} <class 'dict'>
# # 网络传输的str input 输入的时候 sql注入 等等 绝对不能使用eval
#
# # exec 与 eval 几乎一样， 代码流。
# msg = """
# for i in range(10):
#     print(i)
# """
# print(msg)
# print(exec(msg))
#
# # hash: 获取一个对象（可哈希对象：int str ）
# print(hash('sadasdasd'))

# help:查看函数或模块的操作方法
# print(help(str.upper))

# callable 判断一个对象是否可调用
s1 = 'dsadsaad'
# s1()
def func():
    pass
print(callable(s1))  # False
print(callable(func))  # True
