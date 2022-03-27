"""
    练习3：以面向对象思想,描述下列情景.
    玩家攻击敌人,敌人受伤(头顶爆字).

    练习4：以面向对象思想,描述下列情景.
        玩家攻击敌人,敌人受伤(根据玩家攻击力，减少敌人的血量).
"""
class Player:
    def attack(self,target):
        print("攻击")
        target.damage()

class Enemy:
    def damage(self):
        print("头顶爆字")

p01 = Player()
e01 = Enemy()
p01.attack(e01)
