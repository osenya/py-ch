from random import randint
from random import choice
L = [13, 56, 78, 87, 90]

fav_num = choice(L)
print(fav_num)
guess = eval(input('enter a number'))
if guess == fav_num:
    print("you are right!")
else:
    print('you are wrong')

# a program to find the max number


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    else: return num3


print(max_num(156, 78, 45))


def len_con (n):

    length = eval(input('enter the length to be converted'))
    if length < 1:
        print('invalid')
    else:
        length2 = length * 2.54
        return length2


print(len_con(1))

count1 = 0
count2 = 0
for i in range(10):
    num = eval(input('enter any number'))
    if num > 10:
        count1 = count1 + 1
    if num == 0:
        count2 = count2 + 1

print('there are ', count1, 'numbers greater than 10.')
print('there are ', count2, 'numbers equal to zero')


