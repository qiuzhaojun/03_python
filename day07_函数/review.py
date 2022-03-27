"""
    复习 - 容器
        种类：
            字符串：存储字符编码,不可变,序列
            列表：存储变量,可变,序列
            元组：存储变量,不可变,序列
            字典：存储键值对,可变,散列
            集合：存储键,可变,散列
        Python中数据类型种类：
            不可变：按需分配
                整形、浮点型、bool、字符串、元组...
            可变：预留空间+自动扩容
                列表、字典、集合...
        序列与散列：
            序列：有顺序,内存连续,定位灵活(索引切片)
            散列：无顺序,内存分散,定位迅速(键)
        适用性：
            列表：擅长存储单一维度的多个数据
                姓名列表、人数列表....
            字典：擅长存储多个维度的多个数据
                老师信息、疫情信息...
"""
# 创建
dict01 = {"name": "qtx", "age": 18, "money": 99999999}
list01 = ["qtx", "lzmly", "bw"]

# 添加
dict01["sex"] = "男"
list01.append("wwc")

# 定位
print(dict01["name"])
print(list01[0])

# 遍历
for key in dict01:
    print(key)

for value in dict01.values():
    print(value)

for key,value in dict01.items():
    print(key)
    print(value)

for item in list01:
    print(item)

# 从第二个开始到尾
for i in range(1,len(list01)):
    print(list01[i])

# 删除
del dict01["name"]

del list01[0]
list01.remove("lzmly")
