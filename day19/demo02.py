"""
    闭包
        三大要素：
            有内有外
            内访问外
            外返回内
        字面意思:封闭　　内存空间
        作用：外部栈帧执行后不释放,
             等待内部函数执行时使用.
"""


def func01():
    a = 10

    def func02():
        print(a)

    return func02


# 调用外部函数,接收内部函数
result = func01()
# 调用内部函数
result()
