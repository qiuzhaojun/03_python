"""
    函数 - 功能
        创建
            def 函数名(参数):
                函数体

        使用
            函数名(参数)
"""
# 代码的重复是万恶之源

# 做法+用法
"""
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
# ...
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
"""


# 做法
def attack():
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("肘击")

# 用法
# 调试时:希望进入函数内,按F7.
attack()