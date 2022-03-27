"""　
    创建技能类
        实例变量：技能名称　　攻击力　    　法力
                           0--100       0-50
    要求：如果攻击力或者法力超过范围(构建对象的过程失败)
          则在终端中重新输入(重新构建对象)　
"""


class Skill:
    def __init__(self, name="", atk=0, sp=0):
        self.name = name
        self.atk = atk
        self.sp = sp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise Exception("攻击力超过范围", 1001, "if 0 <= value <= 100")

    @property
    def sp(self):
        return self.__sp

    @sp.setter
    def sp(self, value):
        if 0 <= value <= 50:
            self.__sp = value
        else:
            raise Exception("法力超过范围", 1002, "if 0 <= value <= 50")


while True:
    try:
        name = input("请输入技能名称：")
        atk = int(input("请输入攻击力："))
        sp = int(input("请输入法力："))
        skill = Skill(name, atk, sp)
        break
    except Exception as e:
        print("请重新输入")
        print("错误原因：", e.args[0])
        print("错误编号：", e.args[1])
        print("错误代码：", e.args[2])
