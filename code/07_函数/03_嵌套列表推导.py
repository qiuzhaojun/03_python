"""
    列表推导式 嵌套
    练习：exercise07
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["牛奶", "可乐", "雪碧", "咖啡"]
# list_result = []
# # 取
# for r in list01:
#     # 比
#     for c in list02:
#         list_result.append(r + c)
list_result = [r + c for r in list01 for c in list02]
print(list_result)
