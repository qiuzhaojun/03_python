"""
练习：
    1. 在商品列表，获取所有名称与单价
    2. 在商品列表中，获取所有单价小于10000的商品
    3. 对商品列表，根据单价进行降序排列
    4. ([1,1],[2,2,2],[3,3,3])
       获取元组中长度最大的列表
"""
from common.iterator_tools import IterableHelper


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
# 1. 在商品列表，获取所有名称与单价
for item in map(lambda item: (item.name, item.price), list_commodity_infos):
    print(item)

# 列表 = list(可迭代对象)
# 元组 = tuple(可迭代对象)
re = list(map(lambda item: (item.name, item.price), list_commodity_infos))
print(re)

# 2. 在商品列表中，获取所有单价小于10000的商品
for item in filter(lambda item: item.price < 10000, list_commodity_infos):
    print(item.__dict__)

# 3. 对商品列表，根据单价进行降序排列
sorted(list_commodity_infos, key=lambda item: item.price, reverse=True)
for item in list_commodity_infos:
    print(item.__dict__)

# 4. ([1,1],[2,2,2],[3,3,3])
#    获取元组中长度最大的列表
tuple01 = ([1, 1], [2, 2, 2], [3, 3, 3])
print(max(tuple01, key=lambda item: len(item)))
