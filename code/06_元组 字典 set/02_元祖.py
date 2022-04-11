"""
    元组tuple 基础操作
    练习：exercise02
"""
# 创建
# 写法1：元组名 = (数据1, 数据2, 数据3)
tuple_name = ("邱乾清", "刘斯博", "夏锡亮")
# 写法2：元组名 = (数据1, 数据2, 数据3)
# 可变对象(善于改变) --> 不可变对象(节省内存)
list_data = [10, 20, 30]
tuple_result = tuple(list_data)

# 定位
# -- 索引
print(tuple_name[-1])
# -- 切片: 创建新元组
print(tuple_name[:2])

# 遍历
# 从头到为 读取 元素
# 快捷键：iter + 回车
for item in tuple_name:
    print(item)

# 非从头到为 读取 元素
for i in range(len(tuple_name) - 1, -1, -1):
    print(tuple_name[i])

# 注意1：如果元组中只有一个元素,必须加上逗号
    tuple01 = ("数据",)
print(type(tuple01))

# 注意2：构建元组的括号可以省略
tuple02 = "数据1", "数据2", "数据3"
print(tuple02)

# 注意3:序列拆包
a, b, c = (10, 20, 30)
a, b, c = [10, 20, 30]
a, b, c = "孙悟空"
print(a)
print(b)
print(c)
