# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# a. 请将执行函数，并实现让args的值为（1，2，3，4）
# func(1,2,3,4)
# func(*[1,2,3,4])
# b. 请将执行函数，并实现让args的值为([1,2,3,4],[11,22,33])
# func([1,2,3,4],[11,22,33])
# func(*[[1,2,3,4],[11,22,33]])
# c. 请将执行函数，并实现让args的值为([11,22],33)且kwargs的值为{'k1':'v1','k2':'v2'}
# func([11,22],33,k1='v1',k2='v2')
# d. 如执行func(*{'武吉士','尽心','女神'}),请问args和kwargs的值分别是？
# ('武吉士', '女神', '尽心')
# {}
# e. 如执行func({'武吉士','尽心','女神'},[11,22,33]),请问args和kwargs的值分别是？
# ({'武吉士','尽心','女神'},[11,22,33])
# {}
# f. 如执行func('武吉士','尽心','女神',[11,22,33],**{'k1':'栈'}),请问args和kwargs的值分别是？
# ('武吉士','尽心','女神',[11,22,33]）
# {'k1':'栈'})
# func('武吉士','尽心','女神',[11,22,33],**{'k1':'栈','k2':'队列'})
# ('武吉士', '尽心', '女神', [11, 22, 33])
# {'k1': '栈', 'k2': '队列'}
#
#
# def func(name, age=19, email='123@qq.com'):
#     print(name, age, email)
#

# a. 执行func('alex'),判断是否可执行，如可以请问 name、age、email的值分别是？
# func('alex')
# 可以执行 且 name='alex',age=19,email='123@qq.com'
# b. 执行func('alex', 20),判断是否可执行，如可以请问 name、age、email的值分别是？
# func('alex', 20)
# 可以执行 且 name='alex',age=20,email='123@qq.com'
# c. 执行func('alex', 20, 30),判断是否可执行，如可以请问 name、age、email的值分别是？
# func('alex', 20, 30)
# 可以执行 且 name='alex',age=20,email=30
# d. 执行func('alex', email='x@qq.com'),判断是否可执行，如可以请问 name、age、email的值分别是？
# func('alex', email='x@qq.com')
# 可以执行 且 name='alex',age=19,email='x@qq.com'
# e. 执行func('alex', email='x@qq.com', age=99),判断是否可执行，如可以请问 name、age、email的值分别是？
# func('alex', email='x@qq.com', age=99)
# 可以执行 且 name='alex',age=99,email='x@qq.com'
# f. 执行func(name='alex', 99),判断是否可执行，如可以请问 name、age、email的值分别是？
# func(name='alex', 99)  # SyntaxError: positional argument follows keyword argument
# 不可以执行 关键字参数一定要在位置参数后边
# g. 执行func(name='alex', 99, '111@qq.com'),判断是否可执行，如可以请问 name、age、email的值分别是？
# func(name='alex', 99, '111@qq.com') # SyntaxError: positional argument follows keyword argument
# 不可以执行 关键字参数一定要在位置参数后边
# func( 99, '111@qq.com', name='alex') # TypeError: func() got multiple values for argument 'name'
# 前边已经给name一次值，后边又要给值，则报错
# v1 = '武吉士'
# def func():
#     v1 = '京女神'
#     def inner():
#         print(v1)
#     v1 = '萧大侠'
#     inner()
# func()
# v1 = '老男人'
# func()
# 萧大侠
# 萧大侠

