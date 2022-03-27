"""
    函数 - 返回值
        制作函数时  给  使用函数时 传递的信息
        def 函数名(参数):
            ...
            return 数据

        变量 = 函数名(参数)
    练习:exercise11
"""
# 定义函数,两个数字相加.
# number_one = int(input("请输入数字:"))
# number_two = int(input("请输入数字:"))
# result = number_one + number_two
# print(result)


def add(number_one,number_two):
    result = number_one + number_two
    # 不要显示结果
    # 要返回结果
    # print(result)
    return result

data = add(1,2)
print("结果是:"+str(data))
