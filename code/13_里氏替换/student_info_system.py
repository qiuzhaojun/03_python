"""
    学生信息管理系统
"""


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


class StudentView:
    """
        学生信息视图：负责处理界面逻辑
    """

    def __init__(self):
        self.__controller = StudentController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1 添加学生信息")
        print("2 显示学生信息")
        print("3 删除学生信息")
        print("4 修改学生信息")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.__input_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入姓名：")
        stu.age = int(input("请输入年龄："))
        stu.score = int(input("请输入成绩："))
        self.__controller.add_student(stu)


class StudentController:
    def __init__(self):
        self.__all_students = []
        self.start_sid = 1001

    def add_student(self, new_stu):
        # 生成学生编号
        new_stu.sid = self.start_sid
        self.start_sid += 1
        # 存储学生信息
        self.__all_students.append(new_stu)

# 入口
view = StudentView()
view.main()
