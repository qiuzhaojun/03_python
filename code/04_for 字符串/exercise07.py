"""
    练习2：
        循环录入编码值打印文字，直到输入空字符串停止。
            效果：
        请输入数字：113
        q
        请输入数字：116
        t
        请输入数字：
        Process finished with exit code 0
"""
while True:
    str_input = input("请输入数字：")
    if str_input == "":
        break  # 跳出循环
    number = int(str_input)
    print(chr(number))
