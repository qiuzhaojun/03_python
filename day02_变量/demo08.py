"""
    运算符
        增强运算符:在算数运算符基础上,增加对自身赋值的功能
            +=  -=  *=  /=   //=   %=   **=
            累计运算
    练习:exercise09.py

"""
data01 = 5
data01 + 10
print(data01)  # 5

data02 = 5
# data02 = data02 + 10
data02 += 10
print(data02)  # 15
