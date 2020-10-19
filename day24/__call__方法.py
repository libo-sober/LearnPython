# callable(对象)
# 对象() 能不能运行，就是callabele判断的事
class A:
    def __call__(self, *args, **kwargs):
        print('---------------')

obj = A()
print(callable(obj))
obj()  # 对象加括号调用类中的__call__方法
# A()()

# __len__
class Clas:
    def __init__(self, name):
        self.name = name
        self.students = []
    def __len__(self):
        return len(self.students)

py2 = Clas('py2')
py2.students.append('nihao')
py2.students.append('nihao')
py2.students.append('nihao')
# print(len(py2.students))
print(len(py2))