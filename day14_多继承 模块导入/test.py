class A:
    def func01(self):
        print("A - func01")


class B(A):
    def func01(self):
        print("B - func01")
        super(B, self).func01()

b = B()
b.func01()