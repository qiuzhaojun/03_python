region = "湖北"
confirmed = 67802
cure = 63326
cure_rate = 0.99
# message = "%s确诊%d人,治愈%d人,治愈率%.2f%%" % (region, confirmed, cure, cure_rate)
message = f"{region}确诊{confirmed}人,治愈{cure}人,治愈率{cure_rate}%"
print(message)

total_second = 70
print("%d秒是%.2d分零%d秒" % (total_second, total_second // 60, total_second % 60))
print(f"{total_second}秒是{total_second // 60:02}分零{total_second % 60}秒")
