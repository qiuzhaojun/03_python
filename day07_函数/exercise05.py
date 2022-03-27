"""
    对数字列表进行升序排列（小 --> 大）
"""
list01 = [54, 5, 56, 67, 7, 8]

# 取
for r in range(len(list01) - 1):
    # 比
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]

print(list01)
