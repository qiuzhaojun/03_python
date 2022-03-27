"""
    内置生成器
        zip
"""
list_name = ["屠龙刀", "倚天剑", "菜刀"]
list_price = [10000, 10000, 99]
list_cid = [1001, 1002, 1003]


class Commodity:
    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid


# item 是 元组(三个列表每列数据)
for item in zip(list_name, list_price, list_cid):
    print(item)

# list_commodity = []
# for item in zip(list_name, list_price, list_cid):
#     # commodity = Commodity(item[0],item[1],item[2]   )
#     commodity = Commodity(*item)
#     list_commodity.append(commodity)

# 将面向过程的数据,封装为面向对象的数据
list_commodity = [Commodity(*item)
                  for item in zip(list_name, list_price, list_cid)]
print(list_commodity)
# list_datas =[
#     ["屠龙刀", "倚天剑", "菜刀"],
#     [10000, 10000, 99],
#     [1001, 1002, 1003]
# ]
# list_commodity = [Commodity(*item)
#                   for item in zip(*list_datas)]
# print(list_commodity)
