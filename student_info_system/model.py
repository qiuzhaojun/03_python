class StudentModel:
    """
        学生信息模型
    """

    def __init__(self, name="", score=0, age=0, sid=0):
        self.name = name
        self.score = score
        self.age = age
        # 全球唯一标识符：系统为数据赋予的编号
        self.sid = sid

    def __str__(self):
        return "我是%s,编号是%d,年龄是%d,成绩是%d." % (self.name, self.sid, self.age, self.score)