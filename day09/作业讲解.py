def func1():
    print('in func1')


def func2(x):
    print('in func2')
    return x


def func3(y):
    print('in func3')
    return y


ret = func2(func1)  # ret = func1           in func2
ret()  # ret                                in func1
ret2 = func3(func2)  # ret2 = func2         in func3
ret3 = ret2(func1)  # ret3 = func1          in func2
ret3()  # ret3                              in func1


l1 = []


def func(args):
    l1.append(args)
    return l1


print(func(1))  # [1,]
print(func(2))  # [1, 2]
print(func(3))  # [1, 2, 3]
print(l1)  # [1, 2, 3]


def extendList(val, list=[]):
    # 特殊空间的 list=[]
    # list1 = extendList(10) 特殊空间的 list=[10,]
    # list2 = extendList(123, []) 局部list=[123,]
    # list3 = extendList('a') 特殊空间的 list=[10, 'a']
    list.append(val)
    return list


list1 = extendList(10)  # 这里list1是list=[10,]
list2 = extendList(123, [])  # 局部list=[123,]
list3 = extendList('a')  # 这里list3是list1也是list list=[10, 'a']

print(f'list1={list1}')  # 这里list1和list3都是list 而现在的list已经是 list=[10, 'a']
print(f'list2={list2}')  # 返回的局部值list=[123,]
print(f'list3={list3}')  # list=[10, 'a']
