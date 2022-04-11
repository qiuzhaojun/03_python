"""
    练习：将下列英文语句按照单词进行翻转.
    转换前：To have a government that is of people by people for people
    转换后：people for people by people of is that government a have To
"""
message = "To have a government that is of people by people for people"
# 使用空格拆分字符串为列表
list_temp = message.split(" ")
# 使用切片翻转列表,再用空格连接
message = " ".join(list_temp[::-1])
print(message)
