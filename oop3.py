class Employees:
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary


class Insurance:
    def __init__(self, ins_typ, max_cover):
        self.ins_typ = ins_typ
        self.max_cover = max_cover
        self.cover = []

    def add_cover(self, cover):
        if len(self.cover) < self.max_cover:
            self.cover.append(cover)
            return True
        return False


