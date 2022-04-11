"""
    属性原理
        属性 = 读取函数 + 写入函数
"""


class Wife:
    def __init__(self, age=0):
        # 因为先有age的类变量,所以本行代码访问类变量
        self.age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        # 因为被保护
        # 所以实际存储数据的是私有变量__age
        self.__age = value

    # 创建属性对象
    # 绑定读取函数
    # 创建与实例变量名称相同的类变量(类变量先执行)
    age = property(get_age)

    # 调用属性的setter函数
    # 绑定写入函数
    # 将返回值(属性对象)赋值给类变量
    age = age.setter(set_age)


w01 = Wife(25)
print(w01.age)
