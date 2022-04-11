"""
    学生信息管理系统

"""
from typing import List


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
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入姓名：")
        stu.age = int(input("请输入年龄："))
        stu.score = int(input("请输入成绩："))
        self.__controller.add_student(stu)

    def __display_students(self):
        for item in self.__controller.all_students:
            print(item)

    def __delete_student(self):
        sid = int(input("请输入学生编号："))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入学生编号："))
        stu.name = input("请输入学生姓名：")
        stu.score = int(input("请输入学生成绩："))
        stu.age = int(input("请输入学生年龄："))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")


class StudentController:
    def __init__(self):
        self.__all_students = []  # type:List[StudentModel]
        self.start_sid = 1001

    @property
    def all_students(self):
        return self.__all_students

    def add_student(self, new_stu):
        # 生成学生编号
        new_stu.sid = self.start_sid
        self.start_sid += 1
        # 存储学生信息
        self.__all_students.append(new_stu)

    def remove_student(self, sid):
        """
        for item in self.__all_students:
            if item.sid == sid:
                # del item # 删除栈帧中的变量,与列表无关
                # remove内部会再次循环判断需要删除的学生
                self.__all_students.remove(item)
        """
        for i in range(len(self.__all_students)):
            if self.__all_students[i].sid == sid:
                del self.__all_students[i]
                return True  # 表示删除成功,同时退出方法
        return False  # 如果上面没有return,表示删除失败

    def update_student(self, stu):
        for item in self.__all_students:
            if item.sid == stu.sid:
                # item.name = stu.name
                # item.age = stu.age
                # item.score = stu.score
                item.__dict__ = stu.__dict__
                return True
        return False


# 入口
view = StudentView()
view.main()
