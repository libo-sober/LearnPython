# 封装：就是把属性或者方法装起来
# 广义：把属性或者方法装起来，外面不能直接调用了，要通过类名
# 狭义：把属性或者方法装起来，外面不能直接调用了，只能在内部使用
# class A:
#     a = 1
#     b = 2
#
# print(A.a)
# 所有的私有的属性，只能在类的内部去使用
import hashlib
class User:
    def __init__(self, name, password):
        self.user = name
        self.__pwd = password  # 前边加上双下划线，这个变量就是一个私有的属性
    # 外部想看，设置set和get方法
    def __get_md5(self): # 私有方法
        # 外部只能查看不能更改
        md5 = hashlib.md5(self.user.encode('utf-8'))
        md5.update(self.__pwd.encode('utf-8'))
        return md5.hexdigest()
    # 用户必须使用我们指定的方法来修改
    def set_pwd(self, new_pwd):
        self.__pwd = new_pwd
    def get_pwd(self):
        return self.__get_md5()


wang = User('Alex', 'sb')
print(wang.get_pwd())
wang.set_pwd('123')
print(wang.get_pwd())
# 所有的私有化都是为让用户不再外部调用类中的某个名字

# 私有的内容怎么被子类使用？
class Foo:
    def __init__(self):
        self.__func()
    def __func(self):
        print('in Food')
class Son(Foo):
    def __func(self):
        print('in Son')
son = Son()  # in Son
class Foo:
    def __init__(self):
        self.__func()
    def __func(self):
        print('in Food')
class Son(Foo):
    def __func(self):
        print('in Son')
son = Son()  # in Food
# 私有的内容不能在子类中使用， 定义私有，它会自动转换 _类名__私有方法名
