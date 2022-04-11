"""
    练习2：遍历图形控制器
    class GraphicController:
            pass
    controller = CommodityController()
    controller.add_graphic("圆形")
    controller.add_graphic("矩形")
    controller.add_graphic ("三角形")

    for item in controller:
        print(item)
"""


class GraphiceIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.__data) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index]


class GraphicController:
    def __init__(self):
        self.__graphices = []

    def add_graphic(self, graphice):
        self.__graphices.append(graphice)

    def __iter__(self):
        return GraphiceIterator(self.__graphices)


controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")

for item in controller:
    print(item)
