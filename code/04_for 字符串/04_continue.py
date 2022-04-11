"""
    continue
    需求：累加1--100之间的能被3整除的所有整数
    练习:exercise05
"""
sum_value = 0
for number in range(1, 101):
    # 思想：满足条件 干
    if number % 3 == 0:
        sum_value += number
print(sum_value)

sum_value = 0
for number in range(1, 101):
    # 思想：不满足条件 跳   没跳就干
    if number % 3 != 0:
        continue  # 跳过本次循环，继续下次循环
        # break # 跳出
    sum_value += number
print(sum_value)



for i in range(1,5):
    for j in range(1,5):
        if i==1 and j==1 :
            break
            print(i,j)
