"""
    运算符重载
        __add__
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x分量:%d,y分量%d" % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)


pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
print(pos01 + pos02)  # pos01.__add__(pos02)
