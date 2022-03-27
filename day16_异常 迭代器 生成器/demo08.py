"""
    内置生成器
        enumerate
"""
list01 = [43, 54, 65, 6, 7, 89]
# 获取元素
for item in list01:
    print(item)

# 获取索引
for i in range(len(list01)):
    print(list01[i])

# 获取索引 和 元素
for i, item in enumerate(list01):
    print(i, item)

# 需求：将列表中大于10的数字设置为10
for i, item in enumerate(list01):
    if item > 10:
        list01[i] = 10

print(list01)
