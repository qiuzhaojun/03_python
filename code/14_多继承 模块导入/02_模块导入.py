"""
    模块
        导入方式
"""
# 标记项目根目录（蓝色）
# 在文件夹上右键 -> Mark Directory as -> Sources Root

# 方式1：“我过去”
# 语法：import 模块名
# 使用：模块名.成员
# 适用性：更适合面向过程(全局变量、函数)
import module01
module01.func01()

# 方式2：“你过来”
# 语法：from 模块名 import 成员
# 使用：直接使用成员
# 适用性：更适合面向对象(类)
# 注意：导入的成员可能与当前作用域成员冲突
from module01 import func01
from module01 import *

func01()
