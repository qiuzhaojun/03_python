"""
    包中的__init__.py模块
        适用性：导入路径是包时
        作用：决定对外提供包内的什么成员

练习:通过导入包的方式
   在main.py中调用skill_manager.py中实例方法。
   在skill_manager.py中调用list_helper.py中类方法。
"""
# import 包 as p
import package01.package02 as p2
p2.module02.func01()
p2.func03()

import package01 as p1

p1.m2.func01()
p1.func03()
print(p1.data01)