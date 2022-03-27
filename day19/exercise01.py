"""
    练习：画出下列代码内存图
"""


def func01(a):
    def func02():
        nonlocal a
        a += 1
        print(a)

    return func02


result = func01(100)
result()
result()
