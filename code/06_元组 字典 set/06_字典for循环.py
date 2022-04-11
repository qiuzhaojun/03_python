"""
    字典推导式
        字典名 = {键的操作: 值的操作 for 变量 in 可迭代对象 if 条件}
    练习:exercise06
"""
# 需求： key:1-10   value:key的平方
# dict_result = {}
# for number in range(1, 11):
#     dict_result[number] = number ** 2
# print(dict_result)
dict_result = {number: number ** 2 for number in range(1, 11)}

# 需求：将dict_result中偶数键存入另外一个字典
# dict_new = {}
# for key, value in dict_result.items():
#     if key % 2 == 0:
#         dict_new[key] = value
# print(dict_new)
dict_new = {key: value for key, value in dict_result.items() if key % 2 == 0}
