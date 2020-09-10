"""
自定义模块
"""
# 使用__all__控制哪些成员可以被外界使用 只对于 from   import  起作用
__all__ = ['age',
           'age2',
           ]

age = 10

age2 = 20

age3 = 30


def f1():
    print('hello')


# 测试函数，在开发阶段对本模块功能进行测试。
def main():
    print(age)
    f1()


# 可以快速生成 main111
if __name__ == '__main__':
    main()

# 上来就行上下面这些内容
# def main():
#     pass
#
# if __name__ == '__main__':
#     main()
#
