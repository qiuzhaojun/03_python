"""
    练习3：
        删除香港现有人数信息
        删除新疆新增人数信息
        删除上海的新增和现有信息
    练习4：
        在终端中打印香港字典的所有键(一行一个)
        在终端中打印上海字典的所有值(一行一个)
        在终端中打印新疆字典的所有键和值(一行一个)
        在上海字典中查找值是61对应的键名称

"""
dict_HongKong = {
    "region": "香港",
    "new": 15,
    "now": 393,
    "total": 4801,
    "cure": 4320,
    "death": 88
}
del dict_HongKong["now"]
for key in dict_HongKong:
    print(key)

dict_shanghai = {
    "region": "上海",
    "new": 6,
    "now": 61,
    "total": 903,
    "cure": 835,
    "death": 7
}

for value in dict_shanghai.values():
    print(value)

for key, value in dict_shanghai.items():
    if value == 61:
        print(key)
        break  # 如果找到,退出循环.

del dict_shanghai["new"], dict_shanghai["now"]

dict_xinjiang = {
    "region": "新疆",
    "new": 0,
    "now": 49,
    "total": 902,
    "cure": 850,
    "death": 3
}
del dict_xinjiang["new"]
for key, value in dict_xinjiang.items():
    print(key, value)
