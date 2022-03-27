"""
    猜数字2.0版本
        最多猜3次,如果猜中提示恭喜猜对啦
        如果没猜中,提示游戏结束
"""
# 准备一个随机数工具
import random

# 产生一个随机数
random_number = random.randint(1, 100)
print(random_number)
count = 0
while count < 3:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对啦,总共猜了"+str(count)+"次")
        break
else:#
    print("游戏结束")