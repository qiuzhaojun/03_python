"""
    异常处理
        不是解决代码写错的问题,而是解决程序运行后,
        因为数据超过有效范围等原因造成的逻辑错误.
        现象：不再向下继续执行,而是不断向上返回,直到初调用者.
        处理：将异常状态(向上翻),改为正常状态(向下走).
        价值：保障程序能够按照既定流程执行
"""


# 不是代码错误
# print(qtx)   p("hello")

# 而是逻辑错误
# int(input())

# 方式1:"包治百病" (民间喜爱)
# def div_apple(apple_count):
#     try:
#         # ValueError
#         person_count = int(input("请输入人数："))
#         # ZeroDivisionError
#         result = apple_count / person_count
#         print("每人分了", result, "个苹果")
#     except Exception:
#         print("分苹果失败")
#
#
# # 方式2:"对症下药" (官方建议)
# def div_apple(apple_count):
#     try:
#         # ValueError
#         person_count = int(input("请输入人数："))
#         # ZeroDivisionError
#         result = apple_count / person_count
#         print("每人分了", result, "个苹果")
#     except ValueError:
#         print("人数输入有误")
#     except ZeroDivisionError:
#         print("人数不能为零")

# 方式3:无论是否错误,一定执行的逻辑.
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))
        result = apple_count / person_count
        print("每人分了", result, "个苹果")
        # 文件操作
        # 打开
        # 操作
    finally:
        print("分苹果结束了")
        # 关闭

# # 方式4:没有错误才执行的逻辑
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数："))
#         result = apple_count / person_count
#         print("每人分了", result, "个苹果")
#     except ValueError:
#         print("人数输入有误")
#     except ZeroDivisionError:
#         print("人数不能为零")
#     else:
#         print("分苹果成功啦")


div_apple(10)

print("后续逻辑")
