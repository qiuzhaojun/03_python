"""
    两个色子range(1,7)能掷出多少种数字组合
    三个色子range(1,7)能掷出多少种数字组合
"""
# list_result = []
# for x in range(1, 7):  # 1        2      3
#     for y in range(1, 7):  # 123456  123456  123456
#         list_result.append((x, y))

list_result = [(x, y) for x in range(1, 7) for y in range(1, 7)]
print(list_result)

# list_result = []
# for x in range(1, 7):  # 1
#     for y in range(1, 7):  # 1      2     3    ...  6
#         for z in range(1, 7):  # 123456 123456 123456 ...
#             list_result.append((x, y, z))
list_result = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
print(list_result)
