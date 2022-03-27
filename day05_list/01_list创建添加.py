"""
    列表list
        创建
        添加
    练习:exercise03.py
"""
# 1. 创建
# 语法1：列表名 = [数据1, 数据2, 数据3]
list_name = ["邱乾清", "赵屿", "廖显威"]
# 语法2：列表名 = list(可迭代对象)
list_data = list("邱乾清")  # ['邱', '乾', '清']
print(list_data)

# 2. 添加
# 语法1：追加　  列表名.append(数据)
list_name.append("梁煜翀")
list_name.append("不凡")
# 语法2：插入   列表名.insert(索引,数据)
list_name.insert(0,"吴晔")
list_name.insert(2,"吴宗净")

