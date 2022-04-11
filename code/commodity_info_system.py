"""
    创建commodity_info_system.py文件
    创建商品信息管理系统
        Model       -> 封装数据
        View        -> 界面逻辑
        Controller  -> 业务逻辑

    练习1：实现显示所有商品信息
    练习2：实现删除商品信息
    练习3：实现修改商品信息
"""
from typing import List


class CommodityModel:
    """
        商品信息模型
    """

    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return "%s的编号是%d,单价是%d" % (self.name, self.cid, self.price)


class CommodityView:
    """
        商品信息视图
    """

    def __init__(self):
        self.__controller = CommodityController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1 添加商品")
        print("2 显示商品")
        print("3 删除商品")
        print("4 修改商品")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__modify_commodity()

    def __input_commodity(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称：")
        commodity.price = int(input("请输入商品单价："))
        self.__controller.add_commodity(commodity)

    def __display_commoditys(self):
        for item in self.__controller.all_commodity:
            print(item)

    def __delete_commodity(self):
        cid = int(input("请输入商品编号："))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_commodity(self):
        commodity = CommodityModel()
        commodity.cid = int(input("请输入商品编号："))
        commodity.name = input("请输入商品名称：")
        commodity.price = int(input("请输入商品单价："))
        if self.__controller.update_commodity(commodity):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    """
        商品信息控制器
    """

    def __init__(self):
        self.__all_commodity = []  # type:List[CommodityModel]
        self.__start_cid = 1001

    @property
    def all_commodity(self):
        return self.__all_commodity

    def add_commodity(self, commodity):
        """
            添加商品信息
        :param commodity:需要添加的商品信息
        """
        commodity.cid = self.__start_cid
        self.__start_cid += 1
        self.__all_commodity.append(commodity)

    def remove_commodity(self, cid):
        """
            根据商品编号删除商品信息
        :param cid:商品编号
        :return:是否删除成功
        """
        for i in range(len(self.__all_commodity)):
            if self.__all_commodity[i].cid == cid:
                del self.__all_commodity[i]
                return True
        return False

    def update_commodity(self, commodity):
        for item in self.__all_commodity:
            if item.cid == commodity.cid:
                item.__dict__ = commodity.__dict__
                return True
        return False


view = CommodityView()
view.main()
