"""
主逻辑文件
"""
import json
import logging
import time
import datetime
import os
import fileinput

logging.basicConfig(filename='access.log',
                    format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.DEBUG
                    )


write_time = "{yy}年{mm}月{dd}日".format(yy=datetime.datetime.now().year,mm=datetime.datetime.now().month,dd=datetime.datetime.now().day)


def auth (func):                                    #用户登录装饰器
    def inner():
        if login():
            return func()
        else:
            exit("未登录，请先登录")
    return inner


def log(f_log):                                     #日志装饰器
    def inner():
        with open('access.log',encoding='utf-8',mode='a') as f5:
            f5.write("用户：{User}在 {date}执行了%s函数\n".format(User='root',date=write_time,)%(register.__name__))
        return f_log()
    return inner


def login ():                                           #登录功能
    flag = False
    count = 0
    with open('user.json', mode='r', encoding='utf-8') as f1:
        data_r = f1.readlines()
    while True:
        global user
        userlist = {}
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        for i in data_r:
            i=eval(i)
            if i['username'] == user and i['password'] == pwd:
                flag = True
            else:
                pass
        if flag:
            print("登录成功")
            break

        else:
            print("登录失败,请重新登录")
            count += 1
            if count == 3:
                print('您输入的用户密码错误超过3次,已经被锁定,程序已经退出')
                with open('lock.json', mode='a', encoding='utf-8') as f2:
                    userlist['username'] = user
                    userlist['password'] = pwd
                    f2.write(json.dumps(userlist))
                    f2.write('\n')
                    exit()
                return False
    return flag






@log
def register():                                    #注册功能
    with open('user.json', mode='r', encoding='utf-8') as f1:
        data_r = f1.readline()
        dic_r = json.loads(data_r)
        f1.close()

    while True:
        user=input("请输入您要注册的账户：")
        pwd=input("请输入你要注册的账户密码：")
        if user in dic_r['username']:
            print("您注册的账户已经存在请重新输入")
            continue
        else:
            with open('user.json', mode='a', encoding='utf-8') as f1:
                register_list={}
                register_list['username'] = user
                register_list['password'] = pwd
                f1.write(json.dumps(register_list))
                f1.write('\n')
                print("恭喜你注册成功")
        break


@auth                                       #访问文章页面
def wenzhang():
        print('以下是您的博客园页面')
        with open('access.log',mode='a',encoding='utf-8') as f4:
            print("""
            ==================   文章 =====================
            1.文章1
            2.文章2
            3.文章3
            """)
        time.sleep(4)


@auth                                       #访问文章页面
def riji():
        print('以下是您的博客园页面')
        with open('access.log',mode='a',encoding='utf-8') as f4:
            print("""
            ==================   日记 =====================
            1.日记1
            2.日记2
            3.日记3
            """)
            time.sleep(4)


@auth                                       #访问文章页面
def pinglun():
        print('以下是您的博客园页面')
        with open('access.log',mode='a',encoding='utf-8') as f4:
            print("""
            ==================   评论 =====================
            1.评论1
            2.评论2
            3.评论3
            """)
            time.sleep(4)


@auth                                       #访问文章页面
def shoucang():
        print('以下是您的博客园页面')
        with open('access.log',mode='a',encoding='utf-8') as f4:
            print("""
            ==================   收藏 =====================
            1.收藏1
            2.收藏2
            3.收藏3
            """)
            time.sleep(4)


def zhuxiao():
    todelete = []
    zx_user=input("请输入你要注销的账户名：")
    todelete.append(zx_user)
    with fileinput.input('user.json', inplace=True) as f:
        for line in f:
            if all(string not in line for string in todelete):
                print(line, end='')
    print("用户%s已经注销,退出登录" %(zx_user))
    exit()


def run():
    while True:
        print(
            """
                欢迎来到博客园首页
                 1:请登录
                 2:请注册
                 3:文章页面
                 4:日记页面
                 5:评论页面
                 6:收藏页面
                 7:注销
                 8:退出程序
            """)

        first_nmuber = input("请输入号码您要选择的号码：")
        if first_nmuber.isdigit():
            first_nmuber = int(first_nmuber)
            if first_nmuber == 1:
                login()

            elif first_nmuber == 2:
                register()

            elif first_nmuber == 3:
                wenzhang()

            elif first_nmuber == 4:
                riji()

            elif first_nmuber == 5:
                pinglun()

            elif first_nmuber == 6:
                shoucang()

            elif first_nmuber == 7:
                zhuxiao()

            elif first_nmuber == 8:
                print("退出登录")


            else:
                print("您输入的功能不再此清单内，请重新输入")
                continue


if __name__ == "__main__":
    run()