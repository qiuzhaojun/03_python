"""
    需求：
        创建一个员工管理器
            (1) 存储多个员工
            (2) 计算所有员工总薪资
        程序员：底薪 + 项目分红
        测试员：底薪 + Bug数 * 5
        ...
    要求：增加新岗位,员工管理器不变.
    三大特征：
        封装：创建EmployeeManager、Programmer、Tester
        继承：创建Employee隔离创建EmployeeManager与Programmer、Tester的变化
        多态：Programmer、Tester通过重写get_salary方法实现具体薪资计算规则
    设计原则：
        开闭原则：增加新岗位员工,员工管理器不变.
        单一职责：EmployeeManager职责 - 对所有员工的统一操作
                Programmer职责 - 计算程序员的薪资算法
                Tester职责 - 计算测试员的薪资算法
        依赖倒置：EmployeeManager使用Employee，而不使用Programmer、Tester
        组合复用：EmployeeManager与员工薪资算法们是组合(通过变量调用)关系
"""


class Employee:
    def get_salary(self) -> float:
        pass


class EmployeeManager:
    def __init__(self):
        self.__all_employee = []

    def add_employee(self, emp):
        # 添加进来的,必须是员工类型.
        if isinstance(emp, Employee):
            self.__all_employee.append(emp)

    def calculate_total_salary(self):
        """
            计算总薪资
        :return:所有员工的总体薪资
        """
        total_salary = 0
        for emp in self.__all_employee:
            # 调用父
            total_salary += emp.get_salary()
        return total_salary


class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def get_salary(self) -> float:
        # 2. 子重写
        return self.base_salary + self.bonus


class Tester:
    def __init__(self, base_salary, bug_count):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def get_salary(self) -> float:
        return self.base_salary + self.bug_count * 5


manager = EmployeeManager()
# 3. 创建子
manager.add_employee(Programmer(10000, 1000000))
manager.add_employee(Tester(6000, 50))
salary = manager.calculate_total_salary()
print(salary)
