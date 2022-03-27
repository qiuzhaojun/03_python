"""
    练习1：创建敌人类，并保护数据在有效范围内
              数据:姓名/ 攻击力/  血量
                         0-100   0-500
"""


class Enemy:
    def __init__(self, name="", hp=0, atk=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise Exception("攻击力超过范围")

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            value = 0
        elif value > 500:
            value = 500
        self.__hp = value


e01 = Enemy("灭霸", 500, 100)
print(e01.name)
print(e01.hp)
print(e01.atk)
