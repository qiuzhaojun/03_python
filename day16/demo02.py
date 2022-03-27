"""
    迭代
        迭代iter ation：每次获取下一个元素的过程
        迭代器iter ator：执行迭代过程的对象
                具有__next__函数
        可迭代对象iter able：可以被迭代的对象
                具有__iter__函数
"""
message = "我是齐天大圣孙悟空"
# for item in message:
#     print(item)
# for 循环原理
# 1. 获取迭代器对象
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
        # 3. 如果遇到StopIteration错误,则停止.
    except StopIteration:
        break

# 面试题：
# 能够参与for循环的条件是什么?
#   对象具有__iter__函数
#   对象可以获取迭代器对象
