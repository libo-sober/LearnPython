# 多态:用父类直接代替两种子类的类型
# 一个类型表现出来的多种状态
# 支付表现出  微信支付 和 阿里支付 两种状态
# 在Java的情况下:一个参数必须指定类型
# 所以如果想让两个类型的对象都可以传,那么必须让着两个类继承自一个父类,在指定类型的时候使用父类的类型


# 鸭子类型
class list():
    def __init__(self):
        self.length = 0
    def __len__(self):
        pass
    def append(self,num):
        self.append(num)
        self.length += len(num)
l = [1,2,3]
len(l)  # 调用__len__方法
# 所有实现了__len__方法的类,在调用len函数的时候,obj都说是鸭子类型  比如len
# 迭代器 __iter__  __next__ 含有就是







