"""
    闭包应用
        逻辑连续：从得到1000元,到不断购买的过程不中断
"""


def give_gife_money(money):
    print("得到", money, "元压岁钱")

    def child_buy(commodity, price):
        nonlocal money
        money -= price
        print("购买了", commodity, "花了", price, "元", "还剩下", money)

    return child_buy

action = give_gife_money(1000)
action("奥特曼", 300)
action("芭比娃娃", 400)
action("盲盒", 50)
