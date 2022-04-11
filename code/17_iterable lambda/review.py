"""
    迭代
        1. 相关名词
            迭代：每次在之前的基础上,进行重复操作的过程
                例如：遍历容器元素
            迭代器：负责迭代的对象
                具有__next__函数
            可迭代对象：可以返回/创建迭代器的对象
                具有__iter__函数
        2. for循环原理
            迭代器 = 可迭代对象.__iter__()
            while True:
                try:
                    元素 = 迭代器.__next__()
                    处理元素
                except StopIteration:
                    break

        3.class 迭代器:
                def __init__(self,参数)
                    self.数据 = 参数

                def __next__(self):
                    if 没有数据了:
                        raise StopIteration()
                    索引 += 1
                    return self.数据[索引]

            class 可迭代对象:
                def __init__(self,参数):
                    self.数据 = 参数

                def __iter__(self):
                    return 迭代器(self.数据)


    生成器
        价值：推算数据,而不是存储所有结果.
        适用性：返回多个结果
        生成器函数
            语法：
                def 函数名():
                    ....
                    yield 数据
                    ....

                # 不执行函数体
                生成器对象 = 函数名()
                for 变量 in 生成器对象:
                    通过变量操作yield后面的数据


"""