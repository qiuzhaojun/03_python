"""
    列表推导式
        列表 = [对变量操作 for 变量 in 可迭代对象 if 对变量的判断]
        适用性：根据可迭代对象构建列表
    练习:exercise01
"""
# 需求1：将list01中大于10的数字，存入另外一个空列表中
list01 = [4, 54, 56, 67, 8]
# list_result = []
# for item in list01:
#     if item > 10:
#         list_result.append(item)
list_result = [item for item in list01 if item > 10]
print(list_result)

# 需求2：创建列表存储1-10之间数字的立方
# list_result = []
# for number in range(1,11):
#     list_result.append(number ** 3)
list_result = [number ** 3 for number in range(1, 11)]
print(list_result)
