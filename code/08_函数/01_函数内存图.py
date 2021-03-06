"""
    函数内存图
    练习:exercise07~09
"""


# 1. 将函数代码加载到内存图中,但是函数体内部代码不执行.
def func01():
    a = 10


# 2. 调用函数时,在内存中开辟空间(栈帧).
#     存储函数内部创建的变量
func01()


# 3. 函数执行后,该空间立即销毁


def func02(p1, p2):
    p1 = 100 # 修改栈帧中变量
    # 2. 修改可变数据
    p2[0] = 200 # 修改列表中的元素
    # 3. 无需通过返回值传递结果

# 1. 传入可变数据
data01 = 10
data02 = [20]
func02(data01, data02)
print(data01)#?
print(data02)#?
