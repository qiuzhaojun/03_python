"""
5.
# 定义函数,删除商品字典中单价大于5000的所有商品信息
dict_commodity_infos = {
    1001:{"name": "屠龙刀", "price": 10000},
    1002:{"name": "倚天剑", "price": 10000},
    1003:{"name": "金箍棒", "price": 52100},
    1004:{"name": "口罩", "price": 20},
    1005:{"name": "酒精", "price": 30},
}
# 定义函数,删除商品列表中单价大于5000的所有商品信息
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]
"""
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]


def delete_price_gt_5000_by_list():
    for i in range(len(list_commodity_infos) - 1, -1, -1):
        if list_commodity_infos[i]["price"] > 5000:
            del list_commodity_infos[i]


delete_price_gt_5000_by_list()
print(list_commodity_infos)

# 定义函数,删除商品字典中单价大于5000的所有商品信息
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}


# 遍历字典同时删除字典,会报错.
# def delete_price_gt_5000_by_dict():
#     for key,value in dict_commodity_infos.items():
#         if value["price"] > 5000:
#             del dict_commodity_infos[key]

# 遍历列表同时删除字典
def delete_price_gt_5000_by_dict():
    # [(1001, {'name': '屠龙刀', 'price': 10000}), (1002, {'name': '倚天剑', 'price': 10000}), (1003, {'name': '金箍棒', 'price': 52100}), (1004, {'name': '口罩', 'price': 20}), (1005, {'name': '酒精', 'price': 30})]
    list_new_data = list(dict_commodity_infos.items())
    # 遍历列表(字典的键值对)
    for item in list_new_data:
        # item[1] 相当于是字典的值
        if item[1]["price"] > 5000:
            # 　item[0] 相当于是字典的键
            del dict_commodity_infos[item[0]]




delete_price_gt_5000_by_dict()
print(dict_commodity_infos)
