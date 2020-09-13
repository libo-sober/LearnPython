"""
md5加密算法

给一个数据加密的三大步骤：
1.获取一个加密对象
2.使用加密对象的update方法进行加密，加密方法可以调用多次
3.通常通过hexdigest获取加密结果或digest()方法


"""
import hashlib
# # 获取一个加密对象
# m = hashlib.md5()
# # 使用加密对象的update方法进行加密
# m.update('abc中文'.encode('utf-8'))
# m.update('def'.encode('utf-8'))  # 对上面的结果进行累加加密
# # 通过hexdigest获取加密结果
# # res = m.hexdigest()  # 1af98e0571f7a24468a85f91b908d335
# res = m.digest()  # b'/\x1bn)Nr\xd2Z\xe1\x96\xfeJ\xc2\xd2}\xe6'
# print(res)  # 1af98e0571f7a24468a85f91b908d335

# 给一个数据加密，
# 验证：用另一个数据加密的结果和第一次加密的结果对比
# 如果结果相同，说明原文相同。如果不相同，说明原文不同。

# # 不同加密算法：实际上就是加密长度不同。
# s = hashlib.sha224()
# s.update(b'abc')
# print(s.hexdigest())  # 23097d223405d8228642a477bda255b32aadbce4bda0b3f7e36c9da7

# # 在创建加密对象时可以指定参数，称为salt
# m = hashlib.md5(b'abc')
# print(m.hexdigest())
# # 一样
# m = hashlib.md5()
# m.update(b'abc')
# print(m.hexdigest())

# 注册和登录程序：先对输入的用户名和密码进行加密后存入文件防止泄露，
# 然后用户登录后把用户输入的用户名和密码用同样的加密方式加密，
# 把加密后的数据和保存在文件中的加密信息逐条对比，相同登录，否则推出。


def get_md5(username, password):
    m = hashlib.md5()
    m.update(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()


def register(username, password):
    # 加密
    res = get_md5(username, password)
    # 写入文件
    with open('login', mode='at', encoding='utf-8') as f:
        f.write(res + '\n')


def login(username, password):
    # 获取当前登录加密信的结果
    res = get_md5(username, password)
    # 读文件，和其中的数据进行对比
    with open('login', encoding='utf-8') as f:
        for line in f:
            if res == line.strip():
                return True
        else:
            return False


while True:
    op = int(input('1.注册 2.登录 3.退出'))
    if op == 3:
        break
    elif op == 1:
        username = input('输入用户名：')
        password = input('输入密码：')
        register(username, password)
    elif op == 2:
        username = input('输入用户名：')
        password = input('输入密码：')
        res = login(username, password)
        if res:
            print('登录成功！')
        else:
            print('登录失败！')
