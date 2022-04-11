"""
    练习：在终端中输入商品单价、购买的数量和支付金额。
         计算应该找回多少钱。
"""
commodity_price = float(input("请输入商品单价："))
purchase_quantity = float(input("请输入购买数量："))
payment_amount = float(input("请输入支付金额："))
money = payment_amount - commodity_price * purchase_quantity
print("计算应该找回" + str(money) + "元")
