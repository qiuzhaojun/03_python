"""
    继承数据
        1. 子类没有构造函数,继承父类构造函数.
        2. 子类有构造函数,创建子类对象时,使用子类。
           (覆盖了,父类构造函数,好像它不存在)

        class 子类(父类):
            def __init__(self,父类构造函数参数,子类构造函数参数)：
                super().__init__(父类构造函数参数)
                self.数据 = 子类构造函数参数
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

class Student(Person):
    # 子类构造函数:父类构造函数参数,子类构造函数参数
    def __init__(self, name="", age=0, score=0):
        # 通过super函数调用与子类同名的父类方法.
        super().__init__(name, age)
        self.score = score

# 过程：调用子类构造函数,再调用父类构造函数
wk = Student("悟空", 16, 100)
print(wk.name)
print(wk.age)
print(wk.score)
