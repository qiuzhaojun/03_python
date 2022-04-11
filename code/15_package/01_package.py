"""
    python程序结构

    根目录(文件夹)
        包package
            模块
                类
                    函数
                        语句
"""
# 绝对路径：导入包中模块时,路径从项目根目录开始写
#          （不写项目根目录）

# 方式一："我过去"
# import package01.package02.module02 as m
#
# m.func01()

# 方式二："你过来"
from package01.package02.module02 import func01

# from package01.package02.module02 import *
#
func01()
