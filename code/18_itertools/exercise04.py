# 练习:在5张扑克牌中,不考虑顺序抽出3张,有多少可能.
import itertools

list_poker = ["黑桃A", "红桃3", "梅花5", "大王", "红桃K"]
list_result = list(
    itertools.combinations(list_poker, 3))
print(len(list_result))
print(list_result)