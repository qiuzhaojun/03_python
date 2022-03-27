"""
    选择语句
        有选择性的执行
    练习:exercise02
    练习:exercise02
"""
number = int(input("请输入数字："))
if number % 2 != 0:
    print("这是个奇数")
else: # 互斥
    print("这是个偶数")

if float(input("请输入你的存款：")) > 10000000 or int(input("请输入你有几套房：")) > 0:
    print("娶你")
else:
    print("我继续努力")