"""
    练习3：画出下列内存图
        数据拷贝后有1份则互相影响
        数据拷贝后有2份则互不影响
"""
import copy

list01 = ["北京", ["上海", "深圳"]]
list02 = list01  # 赋值
list03 = list01[:]  # 拷贝
list04 = copy.deepcopy(list01)  # 拷贝
list04[0] = "北京04"
list04[1][1] = "深圳04"
print(list01)  # ?
list03[0] = "北京03"
list03[1][1] = "深圳03"
print(list01)  # ?
list02[0] = "北京02"
list02[1][1] = "深圳02"
print(list01)  # ?
