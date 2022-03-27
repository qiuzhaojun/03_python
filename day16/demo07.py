"""
    生成器应用
        价值：
            产生大量数据,不用容器存储.节省内存
        适用性：
            函数向外返回多个数据使用yield
            函数向外返回单个数据使用return
"""
list01 = [4, 4, 565, 67, 7, 8, 89, 90]


# 传统思想：用容器存储所有结果
# def find_gt_10():
#     result = []
#     for number in list01:
#         if number > 10:
#             result.append(number)
#     return result
#
# data = find_gt_10()
# for item in data:
#     print(item)


def find_gt_10():
    for number in list01:
        if number > 10:
            yield number


# 惰性操作/延迟操作 (创建生成器对象 - 推算数据)
# 循环一次 计算一次 返回一次
data = find_gt_10()
for item in data:
    print(item)
