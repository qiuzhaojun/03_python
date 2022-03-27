"""
    自定义迭代器
        需求：for自定义对象
"""


class SkillIterator: # 技能迭代器
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        # 如果索引是最大的或者超过了，则停止迭代
        if self.__index >= len(self.__data) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index]


class SkillController: # 技能可迭代对象
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        return SkillIterator(self.__skills)


controller = SkillController()
controller.add_skill("六脉神剑")
controller.add_skill("降龙十八掌")
controller.add_skill("打狗棍")
controller.add_skill("如来神掌")

# for item in controller:
#     print(item)

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)  #
    except StopIteration:
        break
