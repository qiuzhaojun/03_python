"""
    画出下列代码内存图
"""


class MyClass:
    data02 = 20 # 大家

    def __init__(self):
        self.data01 = 10 # 自己

        self.data01 += 1  # 实例变量自增1
        MyClass.data02 += 1  # 类变量自增1

m01 = MyClass()
m02 = MyClass()
m03 = MyClass()
print(m03.data01)  # 11
print(MyClass.data02)  # 23
