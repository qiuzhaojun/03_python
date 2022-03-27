"""
    数据类型转换
        结果 = 数据类型(待转数据)
    练习:exercise05
"""
# 字符串str   整形int    浮点型float

# input 结果为 字符串类型
# age = int( input("请输入你的年龄：") )
#
# print("明年你"+ str(age + 1) +"岁了")

# 1. 字符串与整数间转换
# str --> int    整数 = int(字符串)
data01 = int("18")
# int --> str    字符串 = str(整数)
data02 = str(18)

# 2. 字符串与浮点型间转换
# str --> float   浮点型 = float(字符串)
data03 = float("1.5")
# float --> str
data05 = str(2.6)

# 3. 整形与浮点型间转换
# int --> float
data06 = float(20)  # 20.0
# float --> int
data07 = int(2.9) # 截断删除(向下取整)
print(data07)

# 4. 注意
# 字符串转换为其他类型时,"一定长得像"对应类型.
# 否则报错
# data08 = float("悟空")

