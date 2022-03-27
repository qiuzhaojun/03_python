"""
    函数参数
        形式参数
            命名关键字形参
"""


# 命名关键字形参:
# 作用：要求必须是关键字实参
# 价值：提高代码可读性
# 写法1：星号元组形参后面的位置形参是命名关键字形参
def func01(*args, p1, p2=0):
    print(args)
    print(p1)
    print(p2)


# func01(1, 2, 3, 4, 5)
func01(1, 2, 3, p1=4, p2=5)
func01(p1=4, p2=5)
func01(p1=4)


# 写法2：星号后面的位置形参是命名关键字形参
# 注意：星号不是参数,只在修饰后面的参数是命名关键字形参
def func02(p1, *, p2=0):
    print(p1)
    print(p2)


func02(p1=4, p2=5)
func02(4, p2=5)
func02(4)

# 命名关键字实参应用：
# def print(*values, sep=' ', end='\n')
# 我叫xx,今年xx岁了.
name = "悟空"
age = 10
# print(f"我叫{name},今年{age}岁了.")
# 因为print第一个参数是星号元组形参
# 所以可以传递无限个位置实参
print("我叫", name, ",今年", age, "岁了.", sep="")
print("*", end=" ")
print("*")

print(1, 2, 3, sep="", end=" ")
# print(1, 2, 3, "", " ")
