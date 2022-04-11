"""
    练习：
    在终端中获取一个3整数，作为边长，打印矩形。
"""
number = int(input("请输入整数："))  # 5
for item in range(number):  # 0 1 2 3 4
    # 如果 开头 或者 末尾
    if item == 0 or item == number - 1:
        print("*" * number)
    else:
        # 空格生成number-2次
        print("*%s*" % (" " * (number - 2)))

# print("*" * number)
# for item in range(number - 2):
#     print("*%s*" % (" " * (number - 2)))
# print("*" * number)
