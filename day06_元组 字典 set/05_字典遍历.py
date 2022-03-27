"""
    遍历
    删除
    练习:exercise05
"""
dict_lsw = {"name": "李世伟", "age": 26, "sex": "男"}
# 1. 遍历
# 语法1：for 键 in 字典名:
for key in dict_lsw:
    print(key)

# 语法2：for 值 in 字典名.values():
for value in dict_lsw.values():
    print(value)

# 语法3：for 键,值 in 字典名.items():
for key, value in dict_lsw.items():
    print(key)
    print(value)

# 如果需要通过索引或者切片操作字典数据
# 那么就要转换为序列(元组,列表)
tuple_keys = tuple(dict_lsw)
tuple_values = tuple(dict_lsw.values())
tuple_k_v = tuple(dict_lsw.items())
print(tuple_k_v)

# 删除  del 字典名[键]
if "sex" in dict_lsw:
    del dict_lsw["sex"]

print(dict_lsw)
