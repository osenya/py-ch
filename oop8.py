class School:
    def __init__(self, first_name, second_name, emp_no):
        self.first_name = first_name
        self.second_name = second_name
        self.emp_no = emp_no

    @property
    def get_fullname(self):
        return 'your name is ={} {}'.format(self.first_name, self.second_name)

    @get_fullname.setter
    def get_fullname(self, name):
        first_name, second_name = name.split(' ')
        self.first_name = first_name
        self.second_name = second_name

    @property
    def get_email(self):
        return self.first_name + self.second_name + '.' + '@gmail.com'

    def __add__(self, other):
        return self.emp_no + other.emp_no


staff1 = School('Boris', 'Johnson', 452)
staff2 = School('Brown', 'Helen', 300)
print(staff1 + staff2)

# doing test on the add method
print(staff1.first_name)

# doing test on the setter property
staff1.get_fullname = 'Mike Jean'

print(staff1.get_email)

x = input('enter any number')
print(x)
x = int(x)
print(x)

# multiple inheritance
# a class can also inherit from two independent classes
# class C(A, B) where the class A and B are not linked together


