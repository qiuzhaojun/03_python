"""
    定义函数,根据年月日,计算星期.
    结果：星期一　　星期二　　星期三　　
"""
import time


def get_week(year, month, day):
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    index_week = tuple_time[6]
    tuple_weeks = ("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
    return tuple_weeks[index_week]


print(get_week(2020, 9, 18))  # 星期五