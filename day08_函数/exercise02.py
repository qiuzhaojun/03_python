"""
    练习3：创建函数,根据课程阶段计算课程名称.
    number = input("请输入课程阶段数：")
    if number == "1":
        print("Python语言核心编程")
    elif number == "2":
        print("Python高级软件技术")
    elif number == "3":
        print("Web全栈")
    elif number == "4":
        print("网络爬虫")
    elif number == "5":
    print("数据分析、人工智能")
"""


# 不建议
# def calculate_name_of_course(number):
#     if number == "1":
#         return "Python语言核心编程"
#     if number == "2":
#       return "Python高级软件技术"
#     if number == "3":
#       return "Web全栈"
#     if number == "4":
#       return "网络爬虫"
#     if number == "5":
#         return "数据分析、人工智能"

# 做法1： 字典实现
# def calculate_name_of_course(number):
#     name_of_course = {
#         "1":"Python语言核心编程",
#         "2":"Python高级软件技术",
#         "3":"Web全栈",
#         "4":"网络爬虫",
#         "5":"数据分析、人工智能"
#     }
#     if number  in name_of_course:
#         return name_of_course[number]

# print(calculate_name_of_course("5"))

# 做法2： 列表实现
def calculate_name_of_course(number):
    """
        计算课程名称
    :param number:int类型,课程阶段数
    :return:课程名称
    """
    name_of_course = [
        "Python语言核心编程",
        "Python高级软件技术",
        "Web全栈",
        "网络爬虫",
        "数据分析、人工智能"
    ]
    if 0 < number <= len(name_of_course):
        return name_of_course[number - 1]


print(calculate_name_of_course(5))
