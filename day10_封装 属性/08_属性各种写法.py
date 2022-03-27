"""
    属性 各种写法
        保护实例变量
            在读写过程中，增加逻辑判断
            只能读取
            只能写入
    练习:exercise05
"""

# 写法1： 读写属性
# 快捷键：props + 回车
"""
class MyClass:
    def __init__(self, data):
        self.data = data # 执行写入函数

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

m01 = MyClass(10)
print(m01.data)
"""

# 写法2： 只读属性
# 快捷键：prop + 回车
# 为私有变量,提供读取功能
"""
class MyClass:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data


m01 = MyClass(10)
print(m01.data)
"""

# 写法3： 只写属性
# 快捷键：无

class MyClass:
    def __init__(self, data):
        self.data = data

    data = property()

    @data.setter
    def data(self, value):
        self.__data = value

    # def set_data(self, value):
    #     self.__data = value
    #
    # data = property(None,set_data)

m01 = MyClass(10)
print(m01.__dict__)

