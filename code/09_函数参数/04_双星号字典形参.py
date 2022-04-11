"""
   函数参数
        形式参数
            双星号字典形参:
"""


# 作用：将多个关键字实参合并为一个字典
# 价值：关键字实参数量无限
def func01(**kwargs):
    print(kwargs)


func01()  # {}
func01(a=1, b=2)  # {'a': 1, 'b': 2}
func01(p1=2, p2=2)  # {'p1': 2, 'p2': 2}


# 应用：万能参数
def func02(*args, **kwargs):
    print(args)
    print(kwargs)


func02()
func02(1, 2, 3)
func02(a=1, b=2)
func02(1, 2, 3, a=1, b=2) 
