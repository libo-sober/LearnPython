# 先读后写 若无文件不会创建新文件
# 读并追加,顺序不能反
# f = open('文件的读写', encoding='utf-8', mode='r+')
# content = f.read()
# print(content)
# f.write('人的一切痛苦,都是对自己无能的愤怒!')
# f.close()

# 优点1:不用手动关闭文件句柄
# # # with open('文件的读', encoding='utf-8') as f1:
# # #     print(f1.read())
# #
# # # 优点2: 一个with可以打开多个open
# # with open('文件的读', encoding='utf-8') as f1,\
# #     open('文件的写', encoding='utf-8', mode='w') as f2:
# #     print(f1.read())
# #     f2.write('dasdasd a')
# #
# # # 缺点:待续.