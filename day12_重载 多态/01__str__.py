"""
    内置可重写函数
        __str__
    体会：
        多态(重写) -- 彰显子类的个性
"""


# 任何类都直接或间接继承自object类
class Person(object):
    def __init__(self, name="", age=0, sex=""):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"我叫{self.name},今年{self.age}岁,性别{self.sex}."

ak = Person("安康", 26, "男")
# <__main__.Person object at 0x7f5ea31cde10>
print(ak)  # 直接打印自定义对象
# 本质：
# 1. 调用自定义对象的__str__
content = ak.__str__()
# 2. 显示返回的字符串
print(content)
