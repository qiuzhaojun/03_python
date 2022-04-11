"""

"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    # 比较是否相同的判断标准：
    def __eq__(self, other):
        return self.cid == other.cid

    # 比较是否大小的判断标准：
    def __lt__(self, other):
        return self.price  <  other.price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

c01 = Commodity(1001, "屠龙刀", 10000)
c02 = Commodity(1001, "屠龙刀", 20000)

# 以下内置函数,需要自定义类重写__eq__
print(c01 == c02)  # true
# count 判断列表中存储在元素数量
print(list_commodity_infos.count(c01))
# print(list_commodity_infos.remove(c01))
print(c01 in list_commodity_infos)

# 以下内置函数,需要自定义类重写__lt__
# list_commodity_infos.sort()
# print(list_commodity_infos)
min_commodity = min(list_commodity_infos)
print(min_commodity.__dict__)