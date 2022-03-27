"""
    删除
    练习:exercise03,04
"""
list_name = ["邱乾清", "赵屿", "廖显威"]
# 语法1：列表名.remove(数据)
# 注意：如果列表没有元素,则报错
if "赵" in list_name:
    list_name.remove("赵")
print(list_name)

# 语法2：del 列表名[索引]  del 列表名[切片]
del list_name[0]
del list_name[:]


