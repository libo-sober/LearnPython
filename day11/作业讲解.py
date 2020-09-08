# 用map来处理字符串列表，把列表中的所有人都变成sb,比方alex_sb
# name = ['oldboy', 'alex', 'wusir']
# ret = map(lambda s: s + '_sb', name)
# print([s + '_sb' for s in name])
# print(list(ret))
#
# 用map来处理下述l，然后用list得到一个新的列表，列表中每日个人的名字都是sb结尾
# l = [{'name': 'alex'}, {'name': 'y'}]
# ret = map(lambda x: x['name'] + '_sb', l)
# print(list(ret))
#
# # 用filter来处理，得到股票价格大于20的股票名字
# shares = {
#     'IBM': 36.6,
#     'Lenovo': 23.2,
#     'oldboy':21.2,
#     'ocaen': 10.2,
# }
# print(list(filter(lambda x: shares[x] > 20, shares)))
# l1 = [1,2,3,4,5,6]
# l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
# tu = ('**', '***', '****', '*******')
# # 写代码，最终得到的是（每个元组第一个元素>2，第三个*至少是4个。）
# # [(3， 'wusir', '****;), (4, '太白', '*******')]这样的数据。得到的列表数据只有这两个元组。
# # lst = [(x, y, z) for x in l1 for y in l2 for z in tu if x > 2 and len(z) >=4]
# # print(lst)
# print(list(filter(lambda x: x[0] > 2 and len(x[-1]) >= 4,zip(l1, l2, tu))))
# l1 = [
#     {'sales_volumn': 0},
#     {'sales_volumn': 108},
#     {'sales_volumn': 337},
#     {'sales_volumn': 475},
#     {'sales_volumn': 396},
#     {'sales_volumn': 173},
#     {'sales_volumn': 58},
#     {'sales_volumn': 9},
#     {'sales_volumn': 77},
#     {'sales_volumn': 342},
#     {'sales_volumn': 231},
#     {'sales_volumn': 23},
# ]
# # 将l1的列表按照列表中的每个字典values大小进行排序，形成一个新的列表
# l2 = sorted(l1, key=lambda x: x['sales_volumn'])
# l3 = sorted(l1, key=lambda x: x['sales_volumn'], reverse=True)
# print(l2)
# print(l3)
#
"""
# 求结果（面试题）
v = [lambda: x for x in range(10)]
print(v)  # 这里面是十个函数的地址
print(v[0])
print(v[0]())  # 相当于执行第一个函数
[<function <listcomp>.<lambda> at 0x000001815FBC8598>, <function <listcomp>.<lambda> at 0x000001816AC94840>, <function <listcomp>.<lambda> at 0x000001816AC948C8>, <function <listcomp>.<lambda> at 0x000001816AC94950>, <function <listcomp>.<lambda> at 0x000001816AC949D8>, <function <listcomp>.<lambda> at 0x000001816AC94A60>, <function <listcomp>.<lambda> at 0x000001816AC94AE8>, <function <listcomp>.<lambda> at 0x000001816AC94B70>, <function <listcomp>.<lambda> at 0x000001816AC94BF8>, <function <listcomp>.<lambda> at 0x000001816AC94C80>]
<function <listcomp>.<lambda> at 0x000001815FBC8598>
9

v = (lambda: x for x in range(10))
print(v)  # 生成器对象
print(v[0])  # 报错
print(v[0]())  # 报错
print(next(v))  # 第一个函数的地址，已经去出来
print(next(v)())  # 取出了第一个，再取就是第二个函数，所以为加括号执行2
# 生成器只是把东西放在那里，并没有执行，next一次执行一次，x增加1
"""
# print(list(map(str, [i + 1 for i in range(9)])))  # 输出什么？
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# 写一个函数完成三次登录功能：
# 用户的用户密码从一个文件register中取出。
# register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中的一行。
# 完成三次验证，三次验证不成功则登录失败，登录失败则返回False。
# 登录成功返回True。


def login():
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    count = 1
    while True:
        with open('register', mode='r', encoding='utf-8') as fp:
            content = fp.readlines()
            for s in content:
                lst = s.strip().split('|')
                if lst[0] == username and lst[1] == password:
                    return True
            else:
                if count == 3:
                    return False
                print('用户名或密码错误！')
                count += 1
                print(f'您还剩余{3 - count + 1}次机会！')
                username = input('请输入用户名：')
                password = input('请输入密码：')


print(login())


# with open('register', mode='r', encoding='utf-8') as fp:
#     content = fp.readlines()
#     for s in content:
#         lst = s.strip().split('|')
#         print(lst[0] == '黄旭' and lst[1] == '98765')
