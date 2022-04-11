"""
    排列
        从n个元素中取出m个元素,并按照顺序进行排列。
        n! / (n-m)!
        语法：
        生成器 = itertools.permutations(可迭代对象,数量)

"""
# 从6个人中取出3个人,演出。
# 6 × 5 × 4  --> 120
list_persons = ["郭德纲", "岳云鹏", "qtx", "孙悟空", "奥特曼", "刘欢"]
import itertools

list_result = list(
    itertools.permutations(list_persons, 3))
print(len(list_result))
print(list_result)
