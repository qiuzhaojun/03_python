"""
    封装行为 - 隐藏
        本质：障眼法
             看似是双下划线开头的变量   __data
             实际是单下划线开头+类名+双下划线开头的变量  _MyClass__data
        注意：类外不能访问,类内可以正常使用.
        私有成员：
            在类中,使用双下划线命名的成员
        适用性：
            不希望类外访问的成员
"""


class MyClass:
    def __init__(self):
        self.__data = 10

    def __func01(self):
        print("func01执行了")
        print("私有变量是：", self.__data)


m01 = MyClass()
print(m01.__dict__)
print(m01._MyClass__data)
print(m01._MyClass__data)

# dir函数可以获取该变量存储的数据所有成员
print(dir(m01))
# m01.__func01()
m01._MyClass__func01()
