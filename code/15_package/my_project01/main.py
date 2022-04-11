"""
    main.py
    需求：
    2.	在main.py中调用skill_manager.py中实例方法。
    3.	在skill_manager.py中调用skill_deployer.py中实例方法。
    4.	在skill_deployer.py中调用list_helper.py中类方法。

"""
from skill_system.skill_manager import SkillManager

manager = SkillManager()
manager.func01()