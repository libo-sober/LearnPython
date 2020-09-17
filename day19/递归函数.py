"""
递归函数
"""
import sys
sys.setrecursionlimit(10000000)  # 改变最大递归深度
count = 0
def func():
    global count
    count += 1
    if count == 3:
        return
    print(count)  # 998
    print(123)
    func()
    print(456)

func()




# RecursionError: maximum recursion depth exceeded while calling a Python object
# 递归最大深度 1000层  节省内存空间，不让用户无线使用内存空间
# 1.递归要尽量少，如果需要很多层才能解决问题，不适合用递归解决
# 2.循环和递归的关系
#   递归不是万能的
#   递归比起循环来说更占用内存
# 修改递归的最大深度
# import sys
# sys.setrecursionlimit(10000000)  # 改变最大递归深度

# 你的递归函数必须要停下来
# 怎么停下来？递归3次结束整个函数

