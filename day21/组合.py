"""
组合
    一个类的对象是另一个类对象的属性
"""
# 学生类
    # 姓名 性别 年龄 学号 班级 手机号
# 班级信息
    # 班级名字 开班是啊金 当前讲师
class Student(object):
    def __init__(self, name, sex, age, number, clas, phone):
        self.name = name
        self.sex = sex
        self.age = age
        self.clas = clas
        self.number = number
        self.phone = phone


class Clas:
    def __init__(self, cname, begint, teacher):
        self.cname = cname
        self.begint = begint
        self.teacheer = teacher


py22 = Clas('python全栈22期', '2019-4-26', '小白')
py23 = Clas('python全栈23期', '2019-5-26', '抱怨')
dazhuang = Student('大壮', 'male', 18, 27, py23, '13838383838')
xuefei = Student('雪非', 'female', 18, 17, py22, '13869696969')

# 查看的是大壮的班级的开班日期是多少
print(dazhuang.clas.begint)
# 查看的是雪非的班级的开班日期是多少

# 对象变成了一个属性  组合
# 课程
# 班级类
    # 包含一个属性 - 课程
# 课程
    # 课程名称
    # 周期
    # 价格
# 创建两个班级 Linux57 python22
# 查看Linux57期的班级所学的课程的价格
# 查看python期的班级所学的课程的周期
class Banji(object):
    def __init__(self, course):
        self.course = course
class Course(object):
    def __init__(self, cname, week, price):
        self.cname = cname
        self.week = week
        self.price = price
linux = Course('linux', 28, 9999)
pytohn = Course('python', 59, 100000)
lin = Banji(linux)
py = Banji(pytohn)

print(lin.course.price)
print(py.course.week)

