"""
    MyRange 3.0 生成器函数
"""
"""
class Generator: # 生成器 = 可迭代对象 + 迭代器
    def __iter__(self): # 可迭代对象
        return self
    
    def __next__(self): # 迭代器
        准备数据
        return 数据
"""


def my_range(stop):
    number = 0
    while number < stop:
        yield number
        number += 1

# for number in my_range(5):
#     print(number)

m01 = my_range(5) # 创建生成器对象Generator()
iterator = m01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break