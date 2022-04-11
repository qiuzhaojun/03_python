"""
    列表嵌套内存图
        浅拷贝

"""
list01 = [10, [20, 30]]
print(id(list01))

list02 = list01[:]# 浅拷贝：复制一层数据
print(id(list02))

list01[0] = 100# 修改第一层数据,互不影响（2份）
print(id(list01[0]))

list01[1][0] = 200 #修改深层数据,互相影响（1份）
print(id(list01[1][0]))
print(id(list02[1][0]))
print(list02) # [10, [200, 30]]


a = [1,2,3]
b = a
b[1] = 0
print(a)