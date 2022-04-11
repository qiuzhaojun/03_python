"""
    组合
        从n个元素中取出m个元素。
        不考虑m个元素的顺序
        语法：
            生成器 = itertools.combinations(可迭代对象, 数量))
"""
# 从6个人中取出4个人,不考虑顺序。
list_persons = ["郭德纲", "岳云鹏", "qtx", "孙悟空", "奥特曼", "刘欢"]
import itertools

list_result = list(
    itertools.combinations(list_persons, 4))
print(len(list_result))
print(list_result)
