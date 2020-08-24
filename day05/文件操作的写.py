# f = open('文件的写', encoding='utf-8', mode='w')
# f.write('随便写一点')
# f.close()

# 如果文件存在，先清空原文件内容，再写入新内容
# f = open('文件的写', encoding='utf-8', mode='w')
# f.write('木子李呢')
# f.close()

# wb
f = open('头像.png', mode='rb')
content = f.read()
# b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00H\x00H\x00.......
# print(content)
f.close()
f1 = open('头像2.png', mode='wb')
f1.write(content)
f1.close()
