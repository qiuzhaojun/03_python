"""
    练习2：定义函数,根据生日(年月日),计算活了多天.
    输入：2010   1   1
    输出：从2010年1月1日到现在总共活了3910天
"""
import time


def life_days(year, month, day):
    # 当前　－　出生时间
    # time_tuple = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    time_tuple = (year, month, day, 0, 0, 0, 0, 0, 0)
    life_second = time.time() - \
                  time.mktime(time_tuple)
    return life_second / 60 / 60 / 24

y = 1990
m = 9
d = 18
result = life_days(y, m, d)
print(f"从{y}年{m}月{d}日到现在总共活了{result:.0f}天")
