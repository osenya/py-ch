from random import choice
from random import randint
titles = ["Engineer", 'Doctor', 'Teacher', 'accountant']
pref_title = choice(titles)
print(pref_title)
guess1 = input('enter your guess')

if guess1 == pref_title:
    print('you are correct')

else:
    print('you have entered the wrong guess')

secret_num = randint(1, 10)
print(secret_num)
ur_guess = 0
while ur_guess != secret_num:
    ur_guess = eval(input('try again'))
print('you finally got it')

