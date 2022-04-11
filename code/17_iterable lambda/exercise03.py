# 练习1：将通用代码放在common/iterable_tools.py中
#       作为静态方法

# 练习2：
#     在列表中查找奇数
#     在列表中查找个位是4 或者 5的元素
from common.iterator_tools import IterableHelper

list01 = [4, 54, 56, 67, 87, 9, 0]

def condtion01(number):
    return number % 2

def condition02(number):
    return number % 10 in (4, 5)

for item in IterableHelper.find_all(list01, condtion01):
    print(item)

for item in IterableHelper.find_all(list01, condition02):
    print(item)