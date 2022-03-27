"""
	练习3：根据下列代码，创建降序排列函数。
    list01 = [5, 15, 25, 35, 1, 2]
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r] < list01[c]:
                list01[r], list01[c] = list01[c], list01[r]
    print(list01)
"""


# 重命名快捷键：shift+f6
# def descending_order(list_target):
#     for r in range(len(list_target) - 1):
#         for c in range(r + 1, len(list_target)):
#             if list_target[r] < list_target[c]:
#                 list_target[r], list_target[c] = list_target[c], list_target[r]
#
#
# list01 = [4, 54, 56, 6, 7, 8]
# descending_order(list01)
# print(list01)
