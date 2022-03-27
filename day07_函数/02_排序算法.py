"""
    排序算法
        思想：
            执行多次计算最大值算法(发现更大的则交换)
        步骤：
            取数据(从头到倒数第二个)
            作比较(从取出的下一个元素开始到末尾)
            判断取出的与比较的
            发现更大则交换
    练习:exercise06
"""
list01 = [3, 54, 56, 6, 67, 78]
# # 让 list01[0] 是最大值
# for c in range(1, len(list01)):
#     if list01[0] < list01[c]:
#         list01[0], list01[c] = list01[c], list01[0]

# # 让 list01[1] 是最大值
# for c in range(2, len(list01)):
#     if list01[1] < list01[c]:
#         list01[1], list01[c] = list01[c], list01[0]

# 让 list01[...] 是最大值 ...

for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]

print(list01)
