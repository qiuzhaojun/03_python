"""
    练习2：
        根据月日,计算是这一年的第几天.
        公式：前几个月总天数 + 当月天数
    例如：5月10日
        计算：31  29  31  30 + 10
"""
month = int(input("请输入月份："))
day = int(input("请输入月份："))

day_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# 累加前几个月
# total_days = 0
# for i in range(month - 1):
#     total_days += day_of_month[i]
total_days = sum(day_of_month[:month - 1])
# 累加当月
total_days += day
print(total_days)
