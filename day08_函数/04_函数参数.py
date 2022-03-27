"""
    函数参数
        实际参数：与形参对应
            位置实参：按顺序
                    函数名(数据1,数据2)
                序列实参：拆分后
                    函数名(*数据)
            关键字实参：按名称
                    函数名(形参名=数据)
                字典实参：拆分后
                    函数名(**数据)
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 1. 位置实参：根据顺序与形参对应
func01(1, 2, 3)
# TypeError: func01() missing 1 required positional argument: 'p3'
# 错误：缺少一个位置实参
# func01(1, 2)

# TypeError: func01() takes 3 positional arguments but 4 were given
# 错误：只需要3个位置实参,但是提供了4个
# func01(1, 2, 3, 4)

# 2. 关键字实参:根据名称与形参对应
func01(p2=2, p1=1, p3=3)
func01(p3=3, p2=2, p1=1)
# 为什么要根据名称对应，请听下回分解.

# func01(p3=3)
# func01(p3=3, p2=2, p1=1,p4 = 4)

# 3. 序列实参：将一个序列拆为多个元素,按顺序与形参对应
list01 = [1, 2, 3]
func01(*list01)

tuple01 = (1, 2, 3)
func01(*tuple01)

str01 = "123"
func01(*str01)

# 4.字典实参：将一个字典拆为多个键值对,按名字与形参对应
dict01 = {"p1": 1, "p3": 3, "p2": 2}
func01(**dict01)
