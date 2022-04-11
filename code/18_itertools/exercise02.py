# 练习：
# 两个色子range(1,7)能掷出多少种数字组合
# 三个色子range(1,7)能掷出多少种数字组合

import itertools

for item in itertools.product(range(1,7),range(1,7)):
    print(item)

# 慎重使用(电脑受不了)
# list_result = list(itertools.product(range(1, 7), repeat=18))
# print(len(list_result))

# 使用生成器(循环一次计算一次返回一次)
for item in itertools.product(range(1, 7), repeat=20):
    print(item)
