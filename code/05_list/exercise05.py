list01 = ["北京", "上海"]
list02 = list01 # 赋值列表地址
list01[0] = "广州"
list03 = list01[:]
list03[-1] = "深圳"
print(list01)#?