"""
    小结-python语言变量
    练习：exercise01
"""
# 全局变量：在文件中创建,全文件可用.
data01 = 10


def func01():
    # 局部变量：在函数中创建,函数内部可用.
    data02 = 20


class MyClass:
    # 类变量:在类中创建,通过类名访问
    data04 = 40

    def __init__(self):
        # 实例变量：在构造函数中通过对象创建,通过对象访问.
        self.data03 = 30


m01 = MyClass()
print(m01.data03)
