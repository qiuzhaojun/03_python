# # 画出下列代码内存图,说出终端显示结果
# name_of_hubei_province = "湖北"
# name_of_hunan_province = "湖南"
# name_of_hunan_province = "湖南省"
# # 将变量赋值给变量：给的是数据地址
# name_of_hunan_province = name_of_hubei_province
# print(name_of_hunan_province)  # 湖北
# name_of_hubei_province = "ss"
# print(name_of_hunan_province)
# print(name_of_hubei_province)

a = 1
b = 2
print(id(a),'\n',id(b))

a = b
print(id(a),'\n',id(b))
print(a,'\n',b)

b = 3
print(id(a),'\n',id(b))
print(a,'\n',b)

a = 3
print(id(a),'\n',id(b))
print(a,'\n',b)
