# 练习1：定义函数,在列表中找出所有偶数
# [43,43,54,56,76,87,98]

# 练习2. 定义函数,在列表中找出所有数字
#  [43,"悟空",True,56,"八戒",87.5,98]

list01 = [43, 43, 54, 56, 76, 87, 98]


def find_even():
    for number in list01:
        if number % 2 == 0:
            yield number


re = find_even()
for item in re:
    print(item)

# 练习2. 定义函数,在列表中找出所有数字
#  [43,"悟空",True,56,"八戒",87.5,98]
list02 = [43, "悟空", True, 56, "八戒", 87.5, 98]


def find_number():
    for number in list02:
        if type(number) in (int, float):
            yield number


re = find_number()
for item in re:
    print(item)
