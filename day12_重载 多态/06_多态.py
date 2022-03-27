"""
    老张开车去东北
        需求变化：飞机、船、小黄车...
        封装：分
            人                车
        继承：隔
                   交通工具
        多态：做
             完成汽车、飞机等具体交通工具的逻辑实现
"""

class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        print("去...")
        # 如果传入的是交通工具
        if isinstance(vehicle, Vehicle):
            # 先确定调用方法
            # 编码时调用的父类
            # 运行时执行的子类
            vehicle.transport()


class Vehicle:
    def transport(self):
        pass


class Car(Vehicle):
    def transport(self):
        print("滴滴滴")


class Airplane(Vehicle):
    def transport(self):
        print("嗖嗖嗖")


zl = Person("老张")
bm = Car()
fj = Airplane()
zl.go_to(bm)
