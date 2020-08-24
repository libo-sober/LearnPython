f1 = open('d:\你想看的都在这.txt', encoding='utf-8', mode='r')
content = f1.read()
print(content)
f1.close()
"""
open 内置函数，open底层调用的是操作系统的接口。
f1 变量 f 文件句柄。 对文件进行的任何操作，都要通过文件句柄.操作函数()的方式。
encoding：参数可以默认不写，默认编码本为操作系统默认的编码。
widows:gbk。
Linux：utf-8。
mac:utf-8。
f1.close() 关闭文件
"""
"""
文件操作三部曲：
1.打开文件
2.对文件句柄进行相应的操作
3.关闭文件
"""