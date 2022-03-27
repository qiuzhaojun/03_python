"""
    封装数据
        多 --> 一
    练习:exercise03
"""

# 面向过程
"""
list_commodity_infos = [ 
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]
# 1.  定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_infos():
    for commodity in list_commodity_infos:
        print(f"编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")
"""


# 面向对象
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

def print_commodity_infos():
    for commodity in list_commodity_infos:
        print(f"编号:{commodity.name},商品名称:{commodity.name},商品单价:{commodity.price}")


print_commodity_infos()
