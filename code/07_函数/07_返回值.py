"""
    返回值 语法
"""


def func01():
    print("func01执行喽")
    return 100


# 调用者可以不接收返回值
func01()
# 调用者也可以接收返回值
re = func01()
print(re)


# 函数没有return默认返回None
# 有return但是后面没有数据,也是默认返回None
def func02():
    print("func02执行喽")
    # return None
    return


re = func02()
print(re)  # None


# return可以退出函数
def func03():
    print("func03执行喽")
    return
    print("func03又执行喽")

func03()
