"""
random模块的演示
"""

import random
# 1. random.random()：获取[0.0,1.0)范围内的浮点数。
print(random.random())

# 2. random.randint(a,b)：获取[a,b]范围内的一个整数。
print(random.randint(5, 9))

# 3. random.uniform(a,b)：获取[a,b)范围内的浮点数。
print(random.uniform(2, 4))

# 4. random.shuffle(x)：把参数指定的数据中的元素混洗，其中参数为变的数据类型。
lst = [i for i in range(10)]
random.shuffle(lst)
print(lst)

# 5. random.sample(x,k)：从x中随机抽取k个数据，组成一个列表返回。
tup = (1, 2, 3, 4, 5, 6)
# random.shuffle(tup)  # TypeError: 'tuple' object does not support item assignment
# 通过random.sample(x,k)变相打乱
lst1 = random.sample(tup, 5)
print(lst1)
