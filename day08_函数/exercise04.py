"""
    练习5：创建函数,计算IQ等级
    ma = int(input("请输入你的心里年龄："))
    ca = int(input("请输入你的实际年龄："))
    iq = ma / ca * 100
    if 140 <= iq:
        print("天才")
    elif 120 <= iq:
        print("超常")
    elif 110 <= iq:
        print("聪慧")
    elif 90 <= iq:
        print("正常")
    elif 80 <= iq:
        print("迟钝")
    else:
        print("低能")
"""


def calculate_iq_grades(ma, ca):
    """

    :param ma:
    :param ca:
    :return:
    """
    iq = ma / ca * 100
    if 140 <= iq: return "天才"
    if 120 <= iq: return "超常"
    if 110 <= iq: return "聪慧"
    if 90 <= iq: return "正常"
    if 80 <= iq: return "迟钝"
    return "低能"

print(calculate_iq_grades(25,26))