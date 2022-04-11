"""
    逻辑运算符
        判断两个命题(bool值)之间的关系
        短路运算
            一但结果确定，后面的语句将不再执行。
            and 有false
            or 有true
    练习:exercise03.py

"""
# True    True
# False    True
# True    False
# False    False

# 与  and  都得满足 结果才满足
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# 来自丈母娘的灵魂质问
# 有钱  and  有房
# print(float(input("请输入你的存款：")) > 10000000 and int(input("请输入你有几套房：")) > 0)

# 或
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

# 有钱  or  有房
print(float(input("请输入你的存款：")) > 10000000 or int(input("请输入你有几套房：")) > 0)

# 非 取反
print(not True)  # False
