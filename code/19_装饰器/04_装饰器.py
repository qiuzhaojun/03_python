"""
    装饰器
        核心价值：拦截
            一个函数如果使用了装饰器,那么再被调用的时候,
            执行的就是装饰器的内部函数.
        适用性：增加的新功能,以后经常会替换。

"""
# 新函数(新功能)
def new_func(func): # 接收旧功能
    def wrapper(): # 包裹新旧功能
        print("new_func执行了")  # 执行新功能
        func()  # 执行旧功能

    return wrapper # 返回包裹函数(不执行新旧功能)

# 原函数(旧功能)
@new_func  # func01 = new_func(func01)
def func01():
    print("func01执行了")

@new_func
def func02():
    print("func02执行了")
# 旧功能 = 新功能 + 旧功能
# func01 = new_func + func01

# 调用外部函数,接收内部函数
# func01 = new_func(func01)

# 调用内部函数
func01()
func02()
