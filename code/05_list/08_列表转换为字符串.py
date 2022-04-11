"""
    1.	列表转换为字符串：
	    result = "连接符".join(列表)
	练习：exercise08
"""
# list01 = ["a", "b", "c"]
# result = "*".join(list01)
# print(result)

# 需求：频繁修改不可变数据
#      (根据某些逻辑,拼接字符串)
# 0 1 2 3 4 5 6 7 8 9

# 缺点：循环一次  产生一个新字符串  之前的数据成为垃圾
# result = ""
# for number in range(10):
#     # result = result + str(number)
#     result += str(number)
# print(result)

# 解决：用可变数据代替不可变数据
result = []
for number in range(10):
    result.append(str(number))
result = "".join(result)
print(result)
