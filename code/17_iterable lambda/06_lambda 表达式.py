"""
    lambda 表达式
        匿名函数:函数没有名称,只有参数与函数体
        语法：lambda 参数:函数体
        与普通函数的异同：
            都是创建函数的技术,
            lambda可以完成的函数都能使用传统函数实现.
            但是lambda不支持:在函数体中赋值
                           函数体中多语句
"""
# 1. 有参数 有返回值
# def func01(p1,p2):
#     return p1 > p2
#
#
# print(func01(1, 2))
func01 = lambda p1, p2: p1 > p2

print(func01(1, 2))

# 2. 有参数 无返回值
# def func02(p1):
#     print("func02执行了,参数是:", p1)
#
#
# func02(100)


func02 = lambda p1: print("func02执行了,参数是:", p1)
func02(100)

# 3. 无参数 有返回值
# def func03():
#     return "大爷"
#
# print(func03())

func03 = lambda: "大爷"
print(func03())

# 4. 无参数 无返回值
# def func04():
#     print("func04执行了")
#
# func04()

func04 = lambda: print("func04执行了")

func04()


# 5. lambda不支持的写法
# (1) 函数体不支持赋值语句
# def func05(p1):
#     p1[0] = 100
#
#
# list01 = [10]
# func05(list01)
# print(list01)  # [100]

# func05 = lambda p1:p1[0] = 100

# (2) 函数体只能有一条语句
# def func06(p1):
#     for item in range(p1):
#         print(item)
#
# func06(5)

# func06 = lambda p1:for item in range(p1): print(item)


