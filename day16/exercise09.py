# 练习1：将列表中所有奇数设置为None
# 练习2：将列表中所有偶数自增1
list01 = [43, 54, 5, 6, 75, 5, 65, 67]
for i, number in enumerate(list01):
    if number % 2:
        list01[i] = None
print(list01)

# 练习2：将列表中所有偶数自增1
# itere + 回车
for i, number in enumerate(list01):
    if number % 2 == 0:
        list01[i] += 1

print(list01)
