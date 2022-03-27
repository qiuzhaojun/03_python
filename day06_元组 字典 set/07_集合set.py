"""
    集合set 基础操作
        作用1：去重复
"""
# 创建
# 语法1：集合名 = {数据1,数据2,数据3}
set_name = {"杨建蒙", "衣俊晓", "杨建蒙", "常磊", "杨建蒙"}
# 语法2：集合名 = {数据1,数据2,数据3}
list01 = [10, 20, 10, 10, 30]
set01 = set(list01)
print(set01)

# 添加
set_name.add("邱乾清")
set_name.add("吴宗净")

# 遍历
for item in set_name:
    print(item)

# 删除
if "吴宗净" in set_name:
    set_name.remove("吴宗净")
