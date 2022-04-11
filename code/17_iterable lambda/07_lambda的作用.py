"""
    lambda的作用
        作为函数的实参
"""

from common.iterator_tools import IterableHelper

list01 = [43, 54, 5, 65, 76, 87, 9]

# def condition01():
#     return item > 10

# for item in IterableHelper.find_all(list01, condition01):
#     print(item)


for item in IterableHelper.find_all(list01,lambda item: item > 10):
    print(item)
