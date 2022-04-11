"""
    列表内存图
    练习：exercise05.py
"""
list01 = [10, 20, 30]
data01 = list01[0]
data02 = list01[:2]# 拷贝新列表
data01 = 100
data02[0] = 200
print(list01)  # [10, 20, 30]
