"""
    练习7：创建函数,根据年月计算天数.
        如果2月是闰年,则29天
        　　　 平年    28

    month = int(input("请输入月份:"))
    if 1 <= month <= 12:
        if month == 2:
            print("29天")
        elif month == 4 or month == 6 or month == 9 or month == 11:
            print("30天")
        else:# 1 3 5 7 8 10 12
            print("31天")
    else:
        print("月份有误")

    year = int(input("请输入年份:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        day = 29
    else:
        day = 28
"""


# def get_day_by_month(year,month):
#     if 1 <= month <= 12:
#         if month == 2:
#             if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#                 return "29天"
#             else:
#                 return "28天"
#         elif month == 4 or month == 6 or month == 9 or month == 11:
#             return "30天"
#         else:
#             return "31天"
#     else:
#         return "月份有误"

# 返回值类型：整数(月份)
# def get_day_by_month(year,month):
#     if 1 <= month <= 12:
#         if month == 2:
#             if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#                 return 29
#             else:
#                 return 28
#         elif month == 4 or month == 6 or month == 9 or month == 11:
#             return 30
#         else:
#             return 31
#     else:
#         return 0

def is_leap_year(year):
    """
        判断年份是否为闰年
    :param year:
    :return:bool类型,True是闰年,Flase不是闰年
    """
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    #     return True
    # else:
    #     return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# def get_day_by_month(year, month):
#     if 1 <= month <= 12:
#         if month == 2:
#             if is_leap_year(year):
#                 return 29
#             else:
#                 return 28
#         elif month == 4 or month == 6 or month == 9 or month == 11:
#             return 30
#         else:
#             return 31
#     else:
#         return 0

def get_day_by_month(year, month):
    """

    :param year:
    :param month:
    :return:
    """
    if month < 1 or month > 12: return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

print(get_day_by_month(2020, 2))
