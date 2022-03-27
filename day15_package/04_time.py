"""
    标准库模块
        time　模块
"""
import time

# 人类的时间　　公园元年　--> 2020 9 18
# 1. 时间元组(年,月,日,时,分,秒,星期,一年的第几天,夏令时)
tuple_time = time.localtime()
print(tuple_time[0])
print(tuple_time[6])
print(tuple_time[3:6])  # 时,分,秒 (15,15,15)

# 机器的时间   1970年元旦 --> 2020 9 18
# 2. 时间戳(从1970年元旦到现在经过的秒数)
print(time.time())  # 1600413415.692054

# 3. 时间戳 --> 时间元组
# 语法： 时间元组 = time.localtime(时间戳)
print(time.localtime(1600413415.692054))

#  时间元组 -> 时间戳
# 语法：时间戳 = time.mktime( 时间元组  )
print(time.mktime(tuple_time))
print(time.mktime((2020, 9, 18, 0, 0, 0, 0, 0, 0)))

# 4. 时间元组　与　字符串
# 时间元组 --> 字符串
# 语法：字符串 = time.strftime(格式,时间元组)
print(time.strftime("%y/%m/%d %H:%M:%S",tuple_time))
print(time.strftime("%Y/%m/%d %H:%M:%S",tuple_time))

# 字符串-->时间元组
# 语法：时间元组 = time.strptime(时间字符串,格式)
print(time.strptime("2020/09/18 15:30:38","%Y/%m/%d %H:%M:%S"))