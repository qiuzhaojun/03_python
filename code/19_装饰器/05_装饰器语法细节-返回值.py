"""
    装饰器语法细节 - 返回值
        内部函数返回值,应该是旧功能的返回值
"""


def new_func(func):
    def wrapper():
        print("new_func执行了")
        result = func()  # 旧功能
        return result

    return wrapper


@new_func
def func01():
    print("func01执行了")
    return 100


@new_func
def func02():
    print("func02执行了")
    return 200


# 调用的是内部函数
re1 = func01()
re2 = func02()

print(re1, re2)
