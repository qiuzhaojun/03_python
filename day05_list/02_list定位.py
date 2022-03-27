"""
    定位
    遍历
    练习:exercise03.py

"""
list_name = ["邱乾清", "赵屿", "廖显威"]
# 一、定位
# 语法1：索引  列表名[整数]
# -- 读取
item = list_name[-1]
# -- 修改
list_name[-1] = "威威"
print(list_name)

# 语法2：切片
# -- 读取：创建了新列表(拷贝)
list_new = list_name[:2]
# -- 修改：遍历右侧可迭代对象,依次存入左侧定位的区域
list_name[:2] = ["清清", "屿屿"]
# list_name[:2] = 100 # 因为100不能for,所以报错
# list_name[:2] = "清清"
# 可以左右两端元素数量不同
# list_name[:2] = "清清清清清清清清清清清清清清"
# list_name[:2] = ""
print(list_name)

# 二、遍历
# 1. 从头到尾读取元素 for 变量名 in 列表名:
for item in list_name:
    print(item)

# 2. 非从头到为读取元素
for i in range(len(list_name)):  # 0 1 2
    list_name[i] = ""

for i in range(len(list_name) - 1, -1, -1):  # 2 1 0
    print(list_name[i])

print(list_name)
