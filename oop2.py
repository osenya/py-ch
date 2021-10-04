class Student:
    def __init__(self, name, age, grade ):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        pass


student_1 = Student('Peter', 22, 95)
student_2 = Student('Mike', 21, 90)
student_3 = Student('Peter', 20, 95)

c1 = Course('science', 3)
c1.add_student(student_1)
c1.add_student(student_2)
print(c1.students[0].name)