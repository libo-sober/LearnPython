# def func():
#     count = 1
#     while 1:
#         count += 1
#         print(count)
#         return
#
#
# func()  # 2


# def func(x, y):
#     return x + y
#
#
# func(1, 6)

# 1.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5.
# def func(s):
#     # count = 0
#     # for i in s:
#     #     count += 1
#     # a = '是'
#     # b = '否'
#     # return a if count > 5 else b
#     return len(s) > 5
# print(func([1,2,3,4,5,6,7,8]))
# print(func('dsandk'))
# print(func((1,2,3)))
# 2.写函数，检测传入字典的每一个value的长度，如果大于2，那么仅保留前两个的内容，并将新内容返回给调用者
# dic = {"k1":"v1v1", "k2":[11,22,33,44]}
# # Ps:字典中的value只能是字符串或列表
# def func(s):
#     for i in s:
#         if len(s[i]) > 2:
#             s[i] = s[i][0:2]
#     return s
# dic = {"k1":"v1v1", "k2":[11,22,33,44]}
# # for s in dic:
# #     print(dic[s][0:2])
# print(func(dic))
# 3.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，
# 然后将这4个内容传入到函数中，此函数接收到四个内容将内容追加到一个student_m文件中
# def func(name, sex, age, education):
#     with open(r"student_m", encoding='utf-8', mode='a+') as f:
#         f.write("%s %s %s %s" % (name, sex, age, education))
# func('李波', '男', 23, "硕士")
# 4.对3题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女
def func(name, age, education, sex='男'):
    with open(r"student_m", encoding='utf-8', mode='a+') as f:
        f.write("%s %s %s %s\n" % (name, sex, age, education))


while True:
    s = input("按照 姓名 年龄 学历 性别 输入学生信息（输入Q或者q推出）：")
    if s.upper() == "Q":
        break
    s = s.strip().split()
    i = len(s)
    if i == 3:
        func(s[0], s[1], s[2])
    else:
        func(s[0], s[1], s[2], s[3])
# 小明 15 高中
# 小花 18 大学 女
# 小王 22 硕士 男
