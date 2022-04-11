from common.iterator_tools import IterableHelper

list01 = [43, 54, 5, 65, 76, 87, 9]


def condition01(item):
    return item > 10


for item in IterableHelper.find_all(list01, condition01):
    print(item)
