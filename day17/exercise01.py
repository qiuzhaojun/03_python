# 练习1：使用生成器表达式在列表中获取所有字符串.
list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
generator01 = (item for item in list01 if type(item) == str)
for item in generator01:
    print(item)

# 练习2：在列表中获取所有整数,并计算它的平方.
generator02 = (item ** 2 for item in list01 if type(item) == int)
for item in generator02:
    print(item)