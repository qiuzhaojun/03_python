"""
    运算符重载
        +=
        对于可变对象,+=应该在原对象基础上改变
        对于不可变对象,+=应该创建新对象
"""

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x分量:%d,y分量%d" % (self.x, self.y)

    # +
    # def __add__(self, other):
    #     x = self.x + other.x
    #     y = self.y + other.y
    #     return Vector2(x, y)

    # +=
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self  # 返回原有数据


pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
print(id(pos01))
pos01 += pos02
print(id(pos01))
print(pos01)

list01 = [1]
# print(id(list01))
list01 += [2]
# print(id(list01))
print(list01)  # [1,2] 在原有列表基础上添加

tuple01 = (1,)
tuple01 += (2,)
print(tuple01)  # (1,2) 产生新容器
