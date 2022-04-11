"""
    老张开车去东北
        需求变化：飞机、船、小黄车...
        封装：分
            人      车
        继承：隔
        多态
    缺点：违反面向对象设计原则 - 开闭
    允许增加新功能,不允许修改客户端代码
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        print("去...")
        # 如果是汽车
        if type(vehicle) == Car:
            vehicle.run()
        # 否则如果是飞机
        elif type(vehicle) == Airplane:
            vehicle.fly()


class Car:
    def run(self):
        print("汽车行驶")


class Airplane:
    def fly(self):
        print("嗖嗖嗖")


zl = Person("老张")
bm = Car()
fj = Airplane()
zl.go_to(bm)
