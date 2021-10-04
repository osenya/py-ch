
file1 = open('file.txt', 'r')

# checking whether the file is readable
print(file1.readable())

# reading the file which basically entails printing all that is written within the file
# print(file1.read())

# reading the first line alone
print(file1.readline())

#  puts all the statement within the file in an array,
# the three denotes the ind ex position
print(file1.readlines()[3])

file1.close()

file_mike = open('file2..txt', 'r')
print(file_mike.readable())
print(file_mike.readlines()[2])

# appending to the end of the file
final_file = open('currents.txt', 'a')

final_file.write('\nc8 = 15')
final_file.close()

# to write to the file / but it will clear the document
# final_file = open('scorecard.txt', 'w')

# final_file.write('\nc8 = 15')
# final_file.close()


def grade_system(marks):
    if marks >= 90:
        student_grade = 'A'
    elif marks >= 80:
        student_grade = 'B'
    elif marks >= 70:
        student_grade = 'C'
    elif marks >= 60:
        student_grade = 'D'
    else:
        student_grade = 'E'

    return student_grade


student_name = input('enter the name of the student')
x = grade_system(eval(input('enter the marks of the student')))
print('The grade of', student_name, 'is', x)
file_score = open('score_sheet.txt', 'a')

file_score.write(student_name)
file_score.write(x)






