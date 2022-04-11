"""
    布尔bool    True  False
        命题：带有判断性质的陈述句
    比较运算符
        ==  >  <   >=  <=  !=
"""
# 命题：你是一个男人
# result = input("请输入你的性别：") == "男"
# print(result)

# 命题：你是一个成年人18  60
result = 18 <= int(input("请输入你的年龄：")) <= 60
print(result)
