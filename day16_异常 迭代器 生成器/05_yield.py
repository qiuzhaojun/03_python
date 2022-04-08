"""
    MyRange 2.0 迭代器 -> yield
"""


class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        number = 0
        while number < self.__stop:
            yield number
            number += 1

m01 = MyRange(5)
iterator = m01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
