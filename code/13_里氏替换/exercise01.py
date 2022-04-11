"""
练习2：创建图形管理器
	1. 记录多种图形（圆形、矩形....）
	2. 提供计算总面积的方法.
    满足：
        开闭原则
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.
    三大特征
        封装：创建GraphicManger、Circle、Rectangle
        继承：创建Graphic类隔离GraphicManger与Circle、Rectangle的变化
        多态：Circle、Rectangle通过重写get_area方法实现具体的面积计算逻辑
    设计原则
        开闭原则：增加了新图形,图形管理器不变
        单一职责：GraphicManger 负责 管理所有图形
                Circle 负责 圆形计算面积
                Rectangle 负责 矩形计算面积
        依赖倒置：GraphicManger调用Graphic
                而不调用Circle、Rectangle
        组合复用：组合关系连接了GraphicManger与具体图形
"""


class GraphicManger:
    def __init__(self):
        self.__all_graphic = []

    def add_graphic(self, graphic):
        if isinstance(graphic, Graphic):
            self.__all_graphic.append(graphic)

    def calcualte_total_area(self):
        total_area = 0
        for item in self.__all_graphic:
            # 先确定了使用方法
            total_area += item.get_area()
        return total_area


class Graphic:
    def get_area(self):
        pass


# --------------------------
class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return self.r ** 2 * 3.14


class Rectangle(Graphic):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def get_area(self):
        return self.l * self.w


manager = GraphicManger()
manager.add_graphic(Circle(5))
manager.add_graphic(Rectangle(2, 3))
print(manager.calcualte_total_area())
