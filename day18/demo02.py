"""
    排列组合
        全排列(笛卡尔积)
        语法：
            生成器 = itertools.product(多个可迭代对象)
        价值：
            需要全排列的数据可以未知
"""
import itertools

list_datas = [
    ["香蕉", "苹果", "哈密瓜"],
    ["牛奶", "可乐", "雪碧", "咖啡"]
]
# 两个列表全排列需要两层循环嵌套
# n              n
list_result = []
for r in list_datas[0]:
    for c in list_datas[1]:
        list_result.append((r, c))
print(list_result)

list_result = list(itertools.product(*list_datas))
print(list_result)
