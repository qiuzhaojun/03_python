"""
    类成员
        类变量
        类方法
    练习:exercise02
"""


class ICBC:
    # 类变量：总行的数据
    total_money = 1000000

    # 类方法：操作类变量
    @classmethod
    def print_total_money(cls):
        # cls 与 类名 相同
        # print(ICBC.total_money)
        print("总行有%d元" % cls.total_money)

    def __init__(self, name="", money=0):
        # 构造函数执行,意味着创建了一家支行
        # 实例变量：某一支行的数据
        self.name = name
        self.money = money
        # 总行的钱减少
        ICBC.total_money -= money

print(ICBC.total_money)
ICBC.print_total_money()


tiantan = ICBC("天坛支行", 100000)
# print(ICBC.total_money)
ICBC.print_total_money()

taoranting = ICBC("陶然亭支行", 200000)
# print(ICBC.total_money)
ICBC.print_total_money()
