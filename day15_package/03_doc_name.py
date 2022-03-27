"""
    模块相关知识
"""

# 1. 模块变量
# (1)文档注释
print(__doc__)

# 会执行review模块的代码(第一次)
import review

# print(review.__doc__)

# 打印主模块(第一次执行的模块)的模块名,一定是__main__
# 打印被导入的模块名,是真实模块名.

print(review.__name__)

# 2. 导入模块是否成功的唯一标准
# 导入路径 + 系统路径 = 真实路径
#　解释：
# (1) 导入路径: import 路径
#              from 路径 import ...
# (2) 系统路径:sys.path
#     [根目录,....]