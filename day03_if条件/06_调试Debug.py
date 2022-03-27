"""
    调试De bug
        让程序中断,审查语句执行流程，并且查看变量取值。
        步骤：
            1. 加断点(在可能出错的行)
            2. 右键Debug
            3. 待断点命中后(蓝色)按F7 或者 F8
    练习:exercise03~07

"""
number = int(input("请输入数字："))
if number > 0:
    print("正数")
elif number < 0:
    print("负数")
else:
    print("是0")
