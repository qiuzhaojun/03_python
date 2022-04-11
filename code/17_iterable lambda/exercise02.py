"""
    练习1：
    需求：
        定义函数，在列表中查找奇数
        定义函数，在列表中查找能被3或5整除的数字
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数find_all
        3. 在当前模块中调用
"""
list01 = [4, 3, 54, 56, 6, 7, 5]


def find_all01():
    for number in list01:
        if number % 2:
            yield number


def find_all02():
    for number in list01:
        if number % 3 == 0 or number % 5 == 0:
            yield number


def condtion01(number):
    return number % 2


def condtion02(number):
    return number % 3 == 0 or number % 5 == 0


def find_all(func_condition):
    for number in list01:
        # if number % 3 == 0 or number % 5 == 0:
        # if condtion02(number):
        if func_condition(number):
            yield number


for item in find_all(condtion01):
    print(item)
