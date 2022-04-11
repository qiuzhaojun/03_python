# 练习：根据下列代码，创建函数。
# 商品字典
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


def print_single_commodity(cid, info):
    print("商品编号%d,商品名称%s,商品单价%d." % (cid, info["name"], info["price"]))


# 1.定义函数，打印所有商品信息,
def print_all_commoditys():
    for key, value in dict_commodity_infos.items():
        print_single_commodity(key, value)


# 2. 定义函数，打印单价大于10000的商品信息,
def print_price_gt_10000_commodity():
    for k, v in dict_commodity_infos.items():
        if v["price"] > 10000:
            print_single_commodity(k, v)


# 3. 定义函数，查找数量最多的订单(使用自定义算法,不使用内置函数)
def find_order_max_by_count():
    max_value = list_orders[0]
    for i in range(1, len(list_orders)):
        if max_value["count"] < list_orders[i]["count"]:
            max_value = list_orders[i]
    return max_value


# 4. 定义函数，根据购买数量对订单列表降序(大->小)排列
def descending_order_by_count():
    for r in range(len(list_orders) - 1):
        for c in range(r + 1, len(list_orders)):
            if list_orders[r]["count"] < list_orders[c]["count"]:
                list_orders[r], list_orders[c] = list_orders[c], list_orders[r]

print_all_commoditys()
print_price_gt_10000_commodity()
find_order_max_by_count()
descending_order_by_count()

