"""
    练习2：定义函数,根据总两数,计算几斤零几两.:
    提示：使用容器包装需要返回的多个数据
    total_liang = int(input("请输入两:"))
    jin = total_liang // 16
    liang = total_liang % 16
    print(str(jin) + "斤零" + str(liang) + "两")
"""
# 函数核心设计理念：
#  崇尚小而精,拒绝大而全.

def calculate_weight(total_liang):
    """
        计算重量
    :param total_liang:int类型，总量数
    :return:tuple类型,(斤,两)
    """
    jin = total_liang // 16
    liang = total_liang % 16
    return jin, liang

tuple_result = calculate_weight(100)
print( f"{tuple_result[0]}斤零{tuple_result[1]}两")
print("%s斤零%s两"%(tuple_result[0],tuple_result[1]))
