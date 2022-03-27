"""
    练习：创建手机类
      数据：品牌、价格、颜色
      行为：通话
      实例化两个对象并调用其函数
      画出内存图
"""


# 命名：所有单词首字母大写,中间不用下划线隔开.
class MobilePhone:
    def __init__(self, brand, price, color=""):
        self.brand = brand
        self.price = price
        # 自动生成代码快捷键：alt + 回车
        self.color = color

    def call(self):
        print(self.brand, "打电话")


huwei = MobilePhone("华为", 5999, "白色")
huwei.call()

iphone = MobilePhone("苹果", 6999, "黑色")
iphone.call()
