"""
    函数式作为参数
        适用性：多段代码,主体相同,核心不同.
        思想：
            分：提取相同代码,分离出不同代码.
            隔：使用参数抽象不同代码,在相同代码中先行确定调用方法(统一)
            做：再增加新的不同代码,添加新函数
"""
list01 = [43, 54, 5, 65, 76, 87, 9]


# 定义函数,在列表中查找所有大于10的数字
def find_all01():
    for item in list01:
        if item > 10:
            yield item


# 定义函数,在列表中查找所有小于50的数字
def find_all02():
    for item in list01:
        if item < 50:
            yield item


# 分-变化的
def condition01(item):
    return item > 10


def condition02(item):
    return item < 50


# 分-相同的
def find_all(func_condition):
    for item in list01:
        # if item < 50:
        # if condition01(item):
        # if condition02(item):
        # 先行确定调用方法
        if func_condition(item):
            yield item


# def condition03(a,b):
#     return a > b

for item in find_all(condition01):
    print(item)
