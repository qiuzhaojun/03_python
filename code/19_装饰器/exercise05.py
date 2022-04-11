"""
    练习2：为sum_data,增加打印函数执行时间的功能.
        函数执行时间公式： 执行后时间 - 执行前时间
    def sum_data(n):
        sum_value = 0
        for number in range(n):
            sum_value += number
        return sum_value

    print(sum_data(10))
    print(sum_data(1000000))
"""
import time


def print_func_time(func):
    def wrapper(*args, **kwargs):
        # 执行后 - 执行前
        start_time = time.time()
        result = func(*args, **kwargs)
        print("函数执行时间是：", time.time() - start_time)
        return result

    return wrapper

@print_func_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(10))
print(sum_data(1000000))
