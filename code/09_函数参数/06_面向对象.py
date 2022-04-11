"""
    面向对象
        用人的思维方式解决软件问题
        找谁？干嘛？

        现实事物 -抽象-> 类(模板) -具体-> 对象
"""


# 老婆类
class Wife:
    # 数据
    def __init__(self, name, height=160, face_score=90):
        self.name = name
        self.height = height
        self.face_score = face_score

    # 行为
    def play(self):
        print(self.name, "在玩耍")

# 创建对象(调用__init__函数)
jn = Wife("建宁", 170, 96)
# 读取对象的颜值
print(jn.face_score)
# 调用对象的行为
jn.play() # play(jn)
