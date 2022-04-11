from bll import StudentController
from model import StudentModel


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

    def __get_number(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print("输入有误")

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入姓名：")
        # stu.age = int(input("请输入年龄："))
        stu.age = self.__get_number("请输入年龄：")
        # stu.score = int(input("请输入成绩："))
        stu.score = self.__get_number("请输入成绩：")
        self.__controller.add_student(stu)

    def __display_students(self):
        for item in self.__controller.all_students:
            print(item)

    def __delete_student(self):
        # sid = int(input("请输入学生编号："))
        sid = self.__get_number("请输入学生编号：")
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        # stu.sid = int(input("请输入学生编号："))
        stu.sid = self.__get_number("请输入学生编号：")
        stu.name = input("请输入学生姓名：")
        stu.score = self.__get_number("请输入学生成绩：")
        stu.age = self.__get_number("请输入学生年龄：")
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")
