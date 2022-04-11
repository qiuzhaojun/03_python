"""
    里氏替换
        - 扩展重写
"""


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_salary(self) -> float:
        return self.base_salary

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
        super().__init__(base_salary)
        self.bonus = bonus

    def get_salary(self) -> float:
        # 2. 子重写
        return super().get_salary() + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def get_salary(self) -> float:
        return super().get_salary() + self.bug_count * 5


manager = EmployeeManager()
# 3. 创建子
manager.add_employee(Programmer(10000, 1000000))
manager.add_employee(Tester(6000, 50))
salary = manager.calculate_total_salary()
print(salary)
