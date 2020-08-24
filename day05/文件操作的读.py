# f = open('文件的读', encoding='utf-8', mode='r')
# content = f.read()
# print(content)
# f.close()
# C:\Users\libo\AppData\Local\Programs\Python\Python36\python.exe D:/WorkSpace/Pycharm/fullstack/day05/文件操作的读.py
# # 你好李波
# # 木子李阿
# # csdnblog
# # hello python
# #
# # Process finished with exit code 0

# read(n) 按字符读取
# f = open('文件的读', encoding='utf-8')
# content = f.read(3)  # 你好李  读前三个字符
# content = f.readline() # 读一行
# content = f.readlines()  # 返回一个列表，列表中的每个元素是源文件的每一行 ['你好李波\n', '木子李阿\n', 'csdnblog\n', 'hello python']
# for 读取
# for line in f:
#     print(line)
# 你好李波
#
# 木子李阿
#
# csdnblog
#
# hello python
#
# print(content)
# f.close()

f = open('头像.png', mode='rb')
content = f.read()
# b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00H\x00H\x00.......
print(content)
f.close()
