"""
    迭代器  --> yield
        练习1:修改商品管理器
        exercise06
"""
class SkillController:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        for item in self.__skills:
            yield item
            print("----")

""" 
    def __iter__(self):
        # 生成迭代器代码的大致规则：
        # 1. 将yield以前的代码定义到__next__函数体中
        # 2. 将yield以后的数据作为__next__函数返回值
        # 3. 最后一个__next__函数在创造异常raise StopIteration()
        print("准备数据")
        yield self.__skills[0]

        print("准备数据")
        yield self.__skills[1]

        print("准备数据")
        yield self.__skills[2]

        print("准备数据")
        yield self.__skills[3]
"""

controller = SkillController()
controller.add_skill("六脉神剑")
controller.add_skill("降龙十八掌")
controller.add_skill("打狗棍")
controller.add_skill("如来神掌")

for item in controller:
    print(item)

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)  #
    except StopIteration:
        break
