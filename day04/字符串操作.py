# # str操作
# s1 = 'python全栈22期'
# # 对字符串进行索引，切片出来的数据都是字符串类型。
# # 从左到右有顺序，下标，索引。
# s2 = s1[0]
# print(s2, type(s2))
# print(s1[-1])  # 最后一个
# print(s1[0:6])  # 顾头不顾尾
# print(s1[6:])  # 取到尾
#
# # 切片，步长
# print(s1[:5:2])  # pto  隔一个取一个
# # 倒序
# print(s1[-1:6:-1])  # 加一个负的步长
# print(s1[::-1])  # 倒序全取
#
# s = 'TaiBai'
# # 字符串操作
# # upper lower
# # 不会对原字符串进行任何操作，产生一个新的字符串
# print(s.upper())  # 全部变大写  TAIBAI
# print(s.lower())  # 全部变小写  taibai
#
# # # 应用：
# # username = input('用户名：')
# # password = input('密码：')
# # code = 'QwEa'
# # your_code = input('请输入验证码（不区分大小写）：')
# # if your_code.lower() == code.lower():
# #     if username == '小明' and password == '123':
# #         print('登录成功')
# #     else:
# #         print('用户名或密码错误')
# # else:
# #     print('验证码错误')
#
# print(s.startswith('t'))  # False
# print(s.startswith('T'))  # Tru
# print(s.startswith('B', 3, 6))  # 索引3到6的部分是不是以B开头 True

# replace
# msg = 'alex很nb,alex是老男孩教育的创始人之一，alex长得很帅啊!'
# msg1 = msg.replace('alex', '太白')  # 默认全部替换
# msg2 = msg.replace('alex', '太白', 2)  # 从左至右替换前两个
# print(msg1)
# print(msg2)

# strip:空白：空格，\t,\n
# s = '     \n太白\t'
# print(s)
# print(s.strip())

# 了解
# 可以去除指定的字符, 只要含有指定字符串中的字符就去除
# s = 'rre太白qsb'
# s1 = s.strip('qrseb')
# print(s1)

# split  非常重要
# str --> list
# s = '太白   女神    吴超'
# l = s.split()
# print(l)  # ['太白', '女神', '吴超']  默认按照空格分隔，返回一个列表
# s1 = '太白:   女神:吴超'
# l1 = s1.split(':')  # 指定分割字符   ['太白', '   女神', '吴超']
# print(l1)
# # 了解：
# s3 = ':barry:nvshen:wu'
# print(s3.split(':'))  # ['', 'barry', 'nvshen', 'wu']
# print(s3.split(':', 2))  # ['', 'barry', 'nvshen:wu']

# # join 非常好用
# s1 = 'alex'
# s2 = '+'.join(s1)
# print(s2, type(s2))  # a+l+e+x  <class 'str'>
# # 前提：列表中的元素必须是字符串类型
# l1 = ['太白', '女神', '吴超']
# print(':'.join(l1))  # 太白:女神:吴超
#
#
# # count
# s8 = 'asdddasaasdadsadasdasdasda'
# print(s8.count('a'))
#
# # format: 格式输出
# # 第一种
# # msg = '我叫{}今年{}性别{}'.format('大壮',25,'男')
# # print(msg)
# # 第二种
# # msg = '我叫{0}今年{1}性别{2}我依然叫{0}'.format('大壮',25,'男')
# # print(msg)
# # 第三种用法
# msg = '我叫{name}今年{age}性别{sex}'.format(name='大壮',sex='男',age=17)
# print(msg)
#
#
# # is 系列
# name = 'taibai123'
# print(name.isalpha())  # 字符串只有字母组成
# print(name.isalnum())  # 字符串由字母或数字组成
# print(name.isdecimal())  # 字符串只由十进制组成

# s1 = input('输入金额')
# if s1.isdecimal():
#     money = int(s1)
# else:
#     print('输入有误')



