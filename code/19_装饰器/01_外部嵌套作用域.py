"""
    Enclosing  外部嵌套作用域 ：函数嵌套。
"""
def func01():
    # 相对于函数外,是局部作用域
    # 相对于内部函数,外部嵌套作用域
    a = 10

    def func02():
        print(a)

    func02()

func01()

def func03():
    a = 10

    def func04():
        # 如果修改外部嵌套变量,必须通过nonlocal声明
        nonlocal a
        a = 20

    func04()
    print(a)  # 20

func03()
