# dictionaries
student = {'Name': 'Mike', 'School': 'Moi University', 'Courses': ['Circuit Theory', 'Project Management']}

print(student)

# accessing the value for one of the keys
print(student['Courses'])

# to add a value
student['Class'] = '2020'

# using the get method to access the key value
print(student.get('School'))

# The prompt when the key is not found
print(student.get('Age', 'Not found'))

# updating our dictionary
student.update({'Name': 'Jack', 'School': 'UoN'})

# to delete a value from the dictionary
del student['School']

# or we can use the pop method
# courses = student.pop('Courses')

print(student.keys())
print(student.values())
print(student.items())

# to loop through the values
for key, value in student.items():
    print(key, value)

