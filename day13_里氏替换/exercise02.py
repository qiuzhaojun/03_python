"""
    参照day11/exercise04
    练习4：以面向对象思想,描述下列情景.
        玩家攻击敌人,敌人受伤
        (根据攻击力，减少血量,掉落装备).

        敌人攻击玩家,玩家受伤
        (根据攻击力，减少血量,闪现红屏).

        要求：
            再增加新角色,之前角色代码不变.

    体会：继承 -- 共性
         多态 -- 个性
"""


class Character:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        print("攻击")
        target.damage(self.atk)

    def damage(self, value):
        self.hp -= value

class Player(Character):

    def damage(self, value):
        super().damage(value)
        print("闪现红屏")

class Enemy(Character):
    def damage(self, value):
        super().damage(value)
        print("掉落装备")

p01 = Player(50,500)
e01 = Enemy(20,100)
p01.attack(e01)
e01.attack(p01)
