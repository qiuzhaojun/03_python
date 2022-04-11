"""
    装饰器语法细节 - 参数
"""


def new_func(func):
    def wrapper(*args, **kwargs):  # 多个实参 合为 一个形参(元组/字典)
        print("new_func执行了")
        result = func(*args, **kwargs)  # 一个实参 拆 多个形参
        return result

    return wrapper


@new_func
def func01(p1):
    print("func01执行了", p1)


@new_func
def func02(p1, p2):
    print("func02执行了", p1, p2)


func01(10)
func02(20, p2 = 30)
