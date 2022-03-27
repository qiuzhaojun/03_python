class Dog:
    def __init__(self, height=0, weight=0):
        self.height = height
        self.weight = weight


d01 = Dog(15, 20)
d02 = d01
d01.height = 17
print(d02.height)  # 17

list_dogs = [
    d01,
    Dog(10, 13),
    Dog(18, 24),
]

for item in list_dogs:
    if item.height > 15:
        item.weight += 5

# 加断点调试看修改后的结果
print(list_dogs)