"""

"""


class CommodityController:
    def __init__(self):
        self.__commoditys = []

    def add_commodity(self, commodity):
        self.__commoditys.append(commodity)

    def __iter__(self):
        for item in self.__commoditys:
            yield item

controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)
