"""
    深拷贝
    练习:exercise07

    为什么要拷贝？
        防止一份数据被"意外"修改
    浅拷贝
        优点：占用内存较少
        缺点：修改深层数据,拷贝前后的数据互相影响
        适用性：不需要修改深层数据
    深拷贝
        优点：随意修改数据,绝对互不影响
        缺点：占用内存过多
        适用性：需要修改深层数据
"""
# 准备拷贝工具
import copy

list01 = [10, [20, 30]]
# 拷贝list01所有依赖的数据
list02 = copy.deepcopy(list01)
list01[0] = 100
list01[1][0] = 200
print(list02)  # ?
