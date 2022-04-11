"""
    练习2：以面向对象的思想，描述以下情景:
    小明在银行取钱（银行钱少了，小明钱多了）
"""


class Person:
    def __init__(self, name="", money=0):
        self.name = name
        self.money = money

    def go_to(self, bank, value):
        print("小明去取钱")
        # 　调用银行取钱功能,传递钱与自身(人)
        bank.draw_money(value, self)


class Bank:
    def __init__(self, money=0):
        self.money = money

    def draw_money(self, value, client):
        # 银行钱少
        self.money -= value
        # 客户钱多
        client.money += value
        print("银行钱：", self.money, "客户钱:", client.money)


xm = Person("小明", 0)
icbc = Bank(100000)
# 小明xm去银行icbc,取100元钱
xm.go_to(icbc, 100)
xm.go_to(icbc, 1000)
xm.go_to(icbc, 10000)
