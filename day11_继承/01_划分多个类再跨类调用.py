"""
    封装设计思想 - 划分多个类,再跨类调用
        需求：老张开车去东北
        划分类：找行为的不同

        分析过程：
            识别对象：
                老张、老李、老孙 --> 属于数据不同,使用对象区分
                    人类
                车类、船类、飞机类、自行车类 --> 属于行为不同,使用类区分
                东北、西北、陕北  --> 属于数据不同,使用对象区分
                    不用做类(因为没有行为需要承担)

            分配职责：
                    人类 --> 去
                    车类 --> 行驶

            建立交互：
                人类 调用 车类

"""


# 做法1：直接创建对象
# 语义：老张每次去东北都使用一辆新车
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, pos):
        print(self.name, "去", pos)
        c = Car()
        c.run()


class Car:
    def run(self):
        print("滴滴滴...")


lz = Person("老张")
lz.go_to("东北")

# 做法2：在构造函数中创建对象
# 语义：老张开自己的车去东北
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.c = Car()

    def go_to(self, pos):
        print(self.name, "去", pos)
        self.c.run()

class Car:
    def run(self):
        print("滴滴滴...")

lz = Person("老张")
lz.go_to("东北")
"""

# 做法3：通过参数传递对象
# 语义：老张通过交通工具(参数)去东北
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, pos, vehicle):
        print(self.name, "去", pos)
        vehicle.run()


class Car:
    def run(self):
        print("滴滴滴...")


lz = Person("老张")
c = Car()
lz.go_to("东北", c)
"""
