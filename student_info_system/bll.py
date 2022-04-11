from typing import List
from model import StudentModel

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