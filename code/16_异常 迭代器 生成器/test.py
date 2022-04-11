class Person:
    def __init__(self,name="",age=0):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age > 1 and age < 150:
            self.__age = age
        else:
            raise Exception("年龄太大或太小",1001,"if value > 0 and value < 150")

class Transport:
    def __init__(self,category="",price=0):
        self.__category = category
        self.__price = price

class car(Transport):
    def __init__(self,oil):
        super().__init__()
        self.__oil = oil

    def calculate(self):
        self.__total = self.__oil * self.__price
        return self.__total

# class airport(Transport):
#     def __init__(self,oil):
#         super().__init__()

if __name__ == "__main__":
    try:
        name = input("请输入姓名")
        age = int(input("请输入年龄"))
        person = Person(name,age)
        print(person.__dict__)
    except Exception as e:
        print(e.args)

