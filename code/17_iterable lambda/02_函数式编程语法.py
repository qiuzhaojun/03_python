"""
    函数式编程语法
"""

# 重要理论支柱：函数可以赋值给变量，赋值后变量绑定函数
def func01():
    print("func01执行喽")

a = func01
a()
func01()

def func02():
    print("func02执行喽")

# 函数赋值给参数,通过参数调用函数
def func03(b):
    print("func03执行喽")
    b()

func03(  func02    )
func03(  func01    )
