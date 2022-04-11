"""
    列表内存图
    练习：exercise05.py
"""
list01 = [10, 20, 30]
print(id(list01))
list01.insert(1,40)
print(id(list01))
# list01.remove(10)
del list01[0]

print(id(list01))

