class Student:
    num_of_students = 0

    def __init__(self, first, last, dept):
        self.first = first
        self.last = last
        self.dept = dept

    @property
    def get_fullname(self):
        return self.first + '  ' + self.last

    @get_fullname.setter
    def get_fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @property
    def get_email(self):
        return self.first + self.last + '.' + '@gmail.com'

    # special methods

    def __repr__(self):
        return "Student details: first name = {}, second name ={}, department = {} ".format(self.first,
                                                                                        self.last, self.dept)

    def __str__(self):
        return "Other details of the student are {}-{}".format(self.get_email, self.get_fullname)

    def __len__(self):
        return len(self.first + self.last)

    # def __add__(self, other):
    # return self.


class Lecturer(Student):
    num_of_lecturers = 0

    def __init__(self, first, last, dept, course_name, students=None):
        super().__init__(first, last, dept)
        self.course_name = course_name
        Lecturer.num_of_lecturers += 1
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            Student.num_of_students += 1
            return True
        return False

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return True
        return False

    def print_stud(self):
        for (i, student) in enumerate(self.students):
            print(i+1, '.', student.get_fullname)


s1 = Student('Mike', 'Osenya', 'Electrical')
s2 = Student('Brian', 'Subaru', 'electrical')
s3 = Student('James', 'Hudson', 'Mechanical;')
s4 = Student('Steve', 'Miller', 'Mechanical;')
s4.get_fullname = 'carie jones'
print(s4.get_email)
s1.first = 'Johnson'

print(s1.get_email)

print(repr(s1))
print(str(s1))
print(len(s1))

l1 = Lecturer('Bill', 'Houston', 'electrical', 'Ece 511')
l2 = Lecturer('John', 'Smith', 'Mechanical', 'MPE 272')
l3 = Lecturer('Don', 'Kennedy', 'Chemical', 'CPE 317')

print(s1.get_email)
print(s1.get_fullname)
print(Lecturer.num_of_lecturers)
print(l1.get_email)
print(l2.get_email)
print(l1.add_student(s1))
print(l1.add_student(s2))
print(l1.add_student(s3))
print(l1.print_stud())

# To check whether an object is an instance of an object
print(isinstance(l1, Lecturer))
print(issubclass(Lecturer, Student))
