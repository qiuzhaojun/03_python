# 练习：得知某人设密码的所有字符"abfghi0123"
#      请排列出6位密码的所有可能
import itertools

list_result = list(
    itertools.permutations("abfghi0123", 6))
print(list_result)
print(len(list_result))
