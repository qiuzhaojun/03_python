"""
   引入 属性@property
   练习:exercise04
"""

# 保护数据有效性
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 23 <= value <= 30:
            self.__age = value
        else:
            raise Exception("我不要")


w01 = Wife("双儿", 25)
w01.age = 10
print(w01.age)

print(w01.__dict__)
