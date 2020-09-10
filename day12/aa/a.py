"""
自定义模块
模块中出现的变量，for循环，if结构，函数定义。。。。成为模块的成员。
"""

# 可执行语句 便明亮定义 函数调用

a = 1


# print(a)

# for x in range(3):
#     print(x)


# 不可执行的 函数定义 类定义
def f():
    print('hello world')


# f()

#  __name__:脚本方式运行时，固定的字符串：__main__
# 以导入方式运行时，就是本模块的名字
# print(__name__)

# 定义一个函数，包含测试语句
def main():
    print(a)
    for x in range(3):
        print(x)
    f()


if __name__ == '__main__':
   main()
