"""
    if 真值表达式
        if 数据:
            该数据如果有值,则满足条件
    练习:exercise08

"""
# 转换为bool类型,结果为false：
# 0   0.0  ""  None
print(bool(None))

message = input("请输入：") # ""
if message:
    print("您输入的是：" + message)
