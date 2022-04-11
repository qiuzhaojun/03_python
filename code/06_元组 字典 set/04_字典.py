"""
    字典dict
    练习:exercise04
"""
# 1. 创建
# 语法1:字典名 = {键1: 值1, 键2: 值2}
dict_lsw = {"name": "李世伟", "age": 26, "sex": "男"}
dict_yjm = {"name": "杨建蒙", "age": 23, "sex": "女"}
# 语法2:字典名 = dict(可迭代对象)
# 注意：可迭代对象内的元素必须能够一分为二
# 　　　[(  ,  ) , (  ,  )]
list01 = ["唐僧", ("猪", "八戒"), ["悟", "空"]]
dict01 = dict(list01)
print(dict01)

# 2. 添加(键不存在)   字典名[键] = 值
if "money" not in dict_lsw:
    dict_lsw["money"] = 10000000

# 3. 定位
# 键　　字典名[键]
# -- 读取
value = dict_lsw["age"]
print(value)
# -- 修改(键存在)
if "age" in dict_lsw:
    dict_lsw["age"] = 38
