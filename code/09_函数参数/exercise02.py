# 练习：定义数值累乘的函数

# list01 = [4,54,5,65,6]
# result = 1
# for item in list01:
#     result *= item
# print(result)

def multiplicative(*args): # 合
    result = 1
    for item in args:
        result *= item
    return result

print(multiplicative(43, 4, 5, 6, 7, 8))
print(multiplicative(43, 4))
print(multiplicative(43, 4))

# 如果调用函数时,只有列表.
# 那么需要通过序列实参拆分后传递
list01 = [4, 5, 5, 6, 8]
multiplicative(*list01) # 拆
