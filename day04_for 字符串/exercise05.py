# 练习：累加10 -- 60之间，个位不是3/5/8的整数和。
# result = 0
# for number in range(10, 61):
#     unit = number % 10
#     if unit != 3 and unit != 5 and unit != 8:
#         result += number
# print(result)  #1255

result = 0
for number in range(10, 61):
    unit = number % 10
    if unit == 3 or unit == 5 or unit == 8:
        continue
    result += number  # 如果需要干的工作代码量大,当前思想代码可读性高.
print(result)  # 1255
