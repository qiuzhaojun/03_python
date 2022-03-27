"""
    Python高级总复习
        一. 程序结构
           1. 导入
            import 模块名
            import 路径.模块名

            from 模块名 import 成员
            from 路径.模块名 import 成员
            路径：从根目录开始(标记为蓝色的文件夹)

            注意：
                import 路径
                from 路径 import 路径
                必须要在包的__init__.py文件中设置
            2. 导入是否成功唯一标准
                导入路径 + 系统路径 = 真实路径
        二.异常处理
            目的：将错误状态改为正常状态

            语法：
                try:
                    可能出错的代码
                except:
                    处理逻辑
        三.生成器
            生成器函数
                def 函数名():
                    ...
                    yield 数据
                    ...

            适用性：返回多个数据使用yield
            原理：
               class 生成器：
                    def __next__(self):
                        "yield"之前的代码
                        return "yield"之后的数据

                    def __iter__(self):
                        return 迭代器()

        四. 迭代器
            class 迭代器：
                def __next__(self):
                    "yield"之前的代码
                    return "yield"之后的数据

            class 可迭代对象:
                def __iter__(self):
                    return 迭代器()

        五.函数式编程
            函数作为参数：传递逻辑(算法 lambda)
            函数作为返回值：逻辑连续(从得到钱到花钱过程不中断)
"""
# 不用设置包的__init__.py
# import package01.module01 as m
#
# m.func01()

# 需要设置__init__.py
# --import package01.module01
# import package01
#
# package01.module01.func01()

# # from package01.module01 import func01
# import package01
# package01.func01()

from package01 import package02

package02.func02()

