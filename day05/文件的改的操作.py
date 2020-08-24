"""
1.以读的模式打开原文件.
2.以写的模式创建一个新文件.
3.将原文件的内容读出来修改成新内容,写入新文件.
4.将原文案金删除.
5.将新文件重命名成原文件.
"""

# 进阶版
import os

with open('alex自述', encoding='utf-8') as f1,\
    open('alex自述.bak', encoding='utf-8', mode='w') as f2:
    for line in f1:
        # 第一次循环 恋爱第1次，第21天后，你找到我说还是喜欢我。我相信了，继续牵着你的手走过校园的每一个角落。
        # old_line = line.strip() # 去除两边空格
        new_line = line.replace('恋爱', 'alex')
        f2.write(new_line)
os.remove('alex自述')
os.rename('alex自述.bak', 'alex自述')

# 有关清空问题:
# 不关闭文件句柄的情况下多次写入是不会清空之前的内容的
