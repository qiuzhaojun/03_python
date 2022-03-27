"""
    2.	字符串转换为列表：
        列表 = “a-b-c-d”.split(“分隔符”)
    练习： exercise09
"""
# result = "a-b-c-d".split("-")
# print(result)

# 需求：拆分一个记录了多个信息的字符串
line = "悟空-唐三藏-八戒"
list_names = line.split("-")
print(list_names)


