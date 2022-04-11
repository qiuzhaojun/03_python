"""
    多继承
        为了隔离多个维度的变化
        同名方法解析顺序：
            类名.mro()
        调用某个父类的同名方法:
            类名.实例方法名(self)
"""


class A:
    def func01(self):
        print("A - func01")


class B(A):
    def func01(self):
        print("B - func01")
        super().func01()


class C(A):
    def func01(self):
        print("C - func01")
        super().func01()

class D(B, C):
    def func01(self):
        print("D - func01")
        # 调用的是Ｂ类型
        super().func01()
        # 调用的是C类型
        C.func01(self)


d = D()
d.func01()  #
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())
