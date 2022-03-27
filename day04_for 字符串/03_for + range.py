"""
    for + range函数
        预定次数的循环 使用 for
        根据条件的循环 使用 while
    练习:exercise04
"""
# 写法1：
# for 变量 in range(开始,结束,间隔):
# 注意：不包含结束值
for number in range(1, 5, 1):  # 1 2 3 4
    print(number)

# 写法2：
# for 变量 in range(开始,结束):
# 注意：间隔默认为1
for number in range(1, 5):  # 1 2 3 4
    print(number)

# 写法3：
# for 变量 in range(结束):
# 注意：开始默认为1
for number in range(5):  # 0 1 2 3 4
    print(number)
