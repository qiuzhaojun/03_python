"""
    练习1：以面向对象思想，描述下列情景：
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图
    封装  继承  多态
"""
# 小鸭子原则：
# 狗    猫
class AttackTarget:
    def damage(self, value):
        pass

class Grenade:
    def __init__(self, atk=0):
        self.atk = atk

    def explode(self, target:AttackTarget):
        print("手雷爆炸")
        # 1.调用父
        target.damage(self.atk)

# -----------------------------------------

class Enemy(AttackTarget):
    # 2.子重写
    def damage(self, value):
        print("头顶爆字")


class Player(AttackTarget):
    def damage(self, value):
        print("碎屏")


grenade = Grenade()
# 3.创建子
grenade.explode(Player())
grenade.explode(Enemy())
