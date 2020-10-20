# 登录
# 蜜罐 假服务器 放爆破  你访问就封你ip
# 认证机制
#   随机发送一个内容：密钥 ： 约定好的一个字符串   解密认证  公钥 私钥
# 生成一个随机字符串
# import os
# ret = os.urandom(16)
# print(ret)
# 替代hashlib模块
import hmac
import os

h = hmac.new(b'alex', os.urandom(32))
ret = h.digest()
print(ret)
