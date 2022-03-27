"""
    容器综合练习
"""
# 商品信息
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]

# 1.打印所有商品信息,
# 格式：商品编号xx,商品名称xx,商品单价xx.
for key, value in dict_commodity_infos.items():
    # print("商品编号%d,商品名称%s,商品单价%d"%(key,value["name"],value["price"]))
    print(f"商品编号{key},商品名称{value['name']},商品单价{value['price']}")

# 2. 打印所有订单中的信息,
# 格式：商品编号xx,购买数量xx.
for item in list_orders:
    print("商品编号%d,购买数量%d." % (item["cid"], item["count"]))

# 3. 打印所有订单中的商品信息,
#    格式：商品名称xx,商品单价:xx,数量xx.
for item in list_orders:
    # item["cid"] --> 1001
    # dict_commodity_infos[1001]
    cid = item["cid"]
    commodity = dict_commodity_infos[cid]
    print(f"商品名称{commodity['name']},商品单价:{commodity['price']},数量{item['count']}.")

# 4. 查找数量最多的订单(使用自定义算法,不使用内置函数)
max_value = list_orders[0]
for i in range(1, len(list_orders)):
    if max_value["count"] < list_orders[i]["count"]:
        max_value = list_orders[i]
print(max_value)

# 5. 根据购买数量对订单列表降序(大->小)排列
for r in range(len(list_orders) - 1):
    for c in range(r + 1, len(list_orders)):
        if list_orders[r]["count"] < list_orders[c]["count"]:
            list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
print(list_orders)
