"""
    6. (选做)根据每人的金条数量,对字典进行升序排列。
    提示：字典 --> 列表 -排序-> 列表 --> 字典
    排列前：
        {"金海":32,"徐天":15,"田丹":0,"柳如丝":500,"铁林":20}
    排列后：
        {'田丹':0,'徐天':15,'铁林':20,'金海':32,'柳如丝':500}
"""
dict_info = {"金海": 32, "徐天": 15, "田丹": 0, "柳如丝": 500, "铁林": 20}
# [('金海', 32), ('徐天', 15), ('田丹', 0), ('柳如丝', 500), ('铁林', 20)]
list_info = list(dict_info.items())
for r in range(len(list_info) - 1):
    for c in range(r + 1, len(list_info)):
        if list_info[r][1] > list_info[c][1]:
            list_info[r], list_info[c] = list_info[c], list_info[r]
dict_info = dict(list_info)
print(dict_info)
