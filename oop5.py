class Ec:
    num_of_students = 0
    weighted_point = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.email = name + '.' + '@gmail.com'
        Ec.num_of_students += 1

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

# how to initiate our subclass with more info than our parent class
# the student class will handle the attribute year


class Student(Ec):
    def __init__(self, name, age, year, no, marks):
        super().__init__(name, age)
        self.year = year
        self.no = no
        self.marks = marks

    def get_marks(self):
        return self.marks

    def get_weighted(self):
        return self.marks/self.weighted_point

    def __add__(self, other):
        return self.marks + other.marks

# it is also possible to give our subclass here its own value of weighted point

    def get_no(self, no):
        return self.no


class Course(Ec):
    def __init__(self, name, age, course_name, students=None):
        super().__init__(name, age)
        self.students = students
        self.course_name = course_name
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_stud(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_stud(self, student):
        if student in self.students:
            self.students.remove(student)

    def print_stud(self):
        for student in self.students:
            print(student)


s1 = Student('Mike', 25, 2020, 2616, 70)
s2 = Student('Frank', 24, 2020, 1616, 80)
print(Ec.num_of_students)
print(s1.email)
print(s1.year)
s1.get_age()
s1.get_no(26/16)
s1.get_name()
s1.weighted_point = 1000  # changing the value of the class variable for this instance
print(s1.get_name() + ',', 'registration number', s1.get_no(2616), 'your score is ', s1.get_marks(), 'and your age is', s1.get_age())
print(s1 + s2)
print(s1.get_weighted())

# getting all the details of the  object
print(s1.__dict__)
