class Employee:
    year = 2020
    num_of_employee = 0

    def __init__(self, first_name, second_name, age, pay):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.pay = pay
        Employee.num_of_employee += 1

    @property
    def full_name(self):
        return self.first_name + ' ' + self.second_name

    @full_name.setter
    def full_name(self, passed_name):
        first_name, second_name = passed_name.spli(' ')
        self.first_name = first_name
        self.second_name = second_name

    def __repr__(self):
        return 'first_name ={}, second_name={}'.format(self.first_name, self.second_name)

    def __str__(self):
        return "other details of the employee are age={} and pay={}".format(self.age, self.pay)

    @property
    def get_email(self):
        return self.first_name + self.second_name + '.' +'@gmail.com'

    @classmethod
    def get_year(cls, yr):
        cls.year = yr
        return cls.year

    @classmethod
    def get_details(cls, emp_details):
        first_name, second_name, age, pay = emp_details.split('-')
        return cls(first_name, second_name, age, pay)


class Managers(Employee):
    num_of_managers = 0
    count1 = 0
    count2 = 0

    def __init__(self, first_name, second_name, age, pay, index, staff_supervised=None):
        super().__init__(first_name, second_name, age, pay)
        self.index = index
        Managers.num_of_managers += 1
        if staff_supervised is None:
            self.staff_supervised = []
        else:
            self.staff_supervised = staff_supervised

    def get_avg(self):

        if self.pay > 50:
            Managers.count1 = Managers.count1 + 1
            print('there are ', Managers.count1, 'with above average salary')
        else:
            Managers.count2 = Managers.count2

    def add_staff(self, staff):
        if staff not in self.staff_supervised:
            self.staff_supervised.append(staff)
            return 'staff added'
        return 'addition failed'

    def remove_staff(self, staff):
        if staff in self.staff_supervised:
            self.staff_supervised.remove(staff)
            return 'staff removed'
        return 'staff not in the list'

    def print_staff(self):
        for staff in self.staff_supervised:
            print(staff.fullname)


class Casual(Employee):
    def __init__(self, first_name, second_name, age, pay, frequency):
        super().__init__(first_name, second_name, age, pay)
        self.frequency = frequency

    # method to initialize
    @classmethod
    def c_details(cls, casual_details):
        first_name, second_name, age, pay, frequency = casual_details.split('-')
        return cls(first_name, second_name, age, pay, frequency)




print(Employee.get_year(2022))
emp_1 = 'Martin-Brown-26-75000'
e1 = Employee.get_details(emp_1)
print(e1.get_email)
print(repr(e1))