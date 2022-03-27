"""
    练习4：以面向对象思想,描述下列情景.
        玩家攻击敌人,敌人受伤(根据玩家攻击力，减少敌人的血量).
"""


class Player:
    def __init__(self, atk):
        self.atk = atk

    def attack(self, target):
        print("攻击")
        target.damage(self.atk)


class Enemy:
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("敌人受伤,血量是:", self.hp)


p01 = Player(10)
e01 = Enemy(100)
p01.attack(e01)
p01.attack(e01)
