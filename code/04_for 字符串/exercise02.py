"""
    程序产生1个,1到100之间的随机数。
        让玩家重复猜测,直到猜对为止。
    每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
    效果：
        请输入要猜的数字:50
    大了
    请输入要猜的数字:25
    小了
    请输入要猜的数字:35
    大了
    请输入要猜的数字:30
    小了
    请输入要猜的数字:32
    恭喜猜对啦,总共猜了5次

"""
# 准备一个随机数工具
import random

# 产生一个随机数
random_number = random.randint(1, 100)
count = 0
while True:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对啦,总共猜了"+str(count)+"次")
        break