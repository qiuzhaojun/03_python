"""
    以容器的思想(统一管理数据)，改造下列代码：
    练习:exercise03
"""
month = int(input("请输入月份："))
# if 1 <= month <= 12:
#     if month == 2:
#         print("29天")
#     # elif month == 4 or month == 6 or month == 9 or month == 11:
#     elif month in (4, 6, 9, 11):
#         print("30天")
#     else:
#         print("31天")
# else:
#     print("月份有误")

# 每月的天数存入容器
day_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
day = day_of_month[month - 1]
print(day)

