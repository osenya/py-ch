student_details1 = ('Name', 'Age', 'Town', 'Mail')
student_details12 = ('Gerald', 22, 'Nairobi', 'gerald@com')

stud_det = dict(zip(student_details1, student_details12))
print(stud_det)

# to add an item to my list
stud_det['school'] = 'Mount Kenya'
print(stud_det)

# to get the value of a key
print(stud_det.get('Town', 'Not in the list'))

# to get key, values and items
print(stud_det.keys())
print(stud_det.values())
print(stud_det.items())
for key, value in stud_det.items():
    print(key, ':', value)


class MyIter:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.first >= self.last:
            raise StopIteration
        current = self.first
        self.first += 1
        return current

# using a generator


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


my_num = my_range(1, 15)
print(next(my_num))
print(next(my_num))
print(next(my_num))



