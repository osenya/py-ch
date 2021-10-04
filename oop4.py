# inheritance example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class RegNo(Student):
    def get_no(self):
        print('Registration number')


class IdNo(Student):
    def get_no2(self,):
        print('id number')


s1 = IdNo('John', 22)
print(s1.get_name())
print(s1.get_age())
print(s1.get_no2())
s2 = RegNo('Peter', 25)
print(s2.get_age())
print(s2.get_name())