"""
shutil模块
loggin 模块
为什么要写log?log是为了排错，用来分析数据
"""
import shutil
# def copy2(src, dst, *, follow_symlinks=True):
# shutil.copy2()
# shutil.copytree(src, dst)
# def rmtree(path, ignore_errors=False, onerror=None):
shutil.rmtree('D:\笔记\作业讲解.py')
# loggin 模块
# 1.用来记录用户的行为---数据分析
# 2.用来记录用户的行为---操作审计
# 3.排查代码中的错误
#
# import logging
# # 输出内容是有等级的：默认处理warnning以上的信息
# import logging
# # import time
# # logging.debug('debug message')  # 调试
# # logging.info('info message')  # 信息
# # logging.warning('warning message')  # 警告
# # logging.error('error message')  # 错误
# # logging.critical('critical message')  # 批判性的
# # # 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG
#
# # 1.无论你想日志输出什么，你都得自己设置，不会自动生成
# # logging.basicConfig()
# # 解决乱码
# fh = logging.FileHandler('tmp.log',encoding='utf-8')
# sh = logging.StreamHandler()
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)d] - %(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     # filename='tmp.log'  # 默认追加
#     handlers=[fh,sh]
# )
#
# logging.warning('warning message 1a的撒旦')
# logging.error('error')
# logging.critical('critical')
