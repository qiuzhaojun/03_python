"""
    while 循环
        延长软件生命
    练习:exercise10
"""
# 死循环
while True:
    state = "奇数" if int(input("请输入整数：")) % 2 else "偶数"
    print("state变量存储的是：" + state)
    if input("按q键退出：") == "q":
        break  # 退出循环
