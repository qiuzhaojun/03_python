"""
    2048 游戏核心算法
"""

list_merge = [2, 0, 2, 0]


# 1. 定义函数　zero_to_end()
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 测试
# zero_to_end()
# print(list_merge)

# zero_to_end()
# print(list_merge)


# 2. 定义合并函数(向左移动的核心算法)　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
def merge():
    """
        合并
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()
    # [4,4,4,4]
    for i in range(len(list_merge) - 1):  # 取前三个  i
        if list_merge[i] == list_merge[i + 1]:  # 与下一个比 i + 1
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]  # 删除下一个(因为不是当前,所以不存在漏删)
            list_merge.append(0)  # 因为删除一个,补充一个,所以不存在越界


merge()
print(list_merge)

# 作业
list_map = [
    [2, 0, 2, 0],
    [2, 0, 0, 2],
    [4, 4, 4, 4],
    [2, 0, 4, 2],
]

# 3. 定义向左移动函数,改变list_map中的数据
#    思路：将list_map每行赋值给list_merge
#         调用合并函数(练习2)

# 4. 定义向右移动函数,改变list_map中的数据
#    思路：将list_map每行,反转,赋值给list_merge
#         调用合并函数
#         将list_merge反转后赋值给list_map
# 温馨提示：画内存图哦
