"""
    main.py
    练习:通过导入包的方式
       在main.py中调用skill_manager.py中实例方法。
       在skill_manager.py中调用list_helper.py中类方法。
"""
# 导入 包
import skill_system

# 包可以访问的成员取决于包的__init__.py
# 因为提供了模块
manager = skill_system.skill_manager.SkillManager()
# 因为提供了类
# manager = skill_system.SkillManager()

manager.func01()