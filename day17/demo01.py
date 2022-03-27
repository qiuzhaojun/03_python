"""
    生成器表达式
    复习：列表推导式
"""
# 需求1：将list01中大于10的数字，存入另外一个空列表中
list01 = [4, 54, 56, 67, 8]
# list_result = []
# for item in list01:
#     if item > 10:
#         list_result.append(item)
list_result = [item for item in list01 if item > 10]
print(list_result)

# def find01():
#     for item in list01:
#         if item > 10:
#             yield item

generator01 = (item for item in list01 if item > 10)
for item in generator01:
    print(item)

# 需求2：创建列表存储1-10之间数字的立方
# 数据
list_result = [number ** 3 for number in range(1, 11)]
# 数据的推算
generator02 = (number ** 3 for number in range(1, 11))
