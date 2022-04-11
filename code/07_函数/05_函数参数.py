"""
    函数参数
        使用函数 给 制作函数 传递的信息
"""


# 制作
# 形式参数：表面/抽象,不真实/不具体的数据
def attack(number):
    for count in range(number):
        print("直拳")
        print("摆拳")
        print("勾拳")
        print("肘击")


# 使用
# 实际参数：真实/具体的数据
attack(2)
attack(5)
