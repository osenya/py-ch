from random import randint

max_temp = 37
temp = eval(input('enter the value of the temperature'))
while temp >= max_temp:
    temp = eval(input('incorrect value.Enter the correct value temperature '))
print('normal temperature ')

secret_num = randint(1, 100)
print(secret_num)
num_guesses = 0
guess = 0

while guess != secret_num and num_guesses <= 4:
    guess = eval(input('Enter your guess'))
    num_guesses = num_guesses + 1
    if guess < secret_num:
        print('Higher. ', 5-num_guesses, 'guesses are left')
    elif guess > secret_num:
        print('LOWER. ', 5-num_guesses, 'guesses are left')
else:
    print('you got it')

if num_guesses == 5 and guess != secret_num:
    print('You lose. The correct number is', secret_num)

i = 1
while i <= 50:
    i = i+1
    print(i)

weight = 0
while weight <= 0:
    weight = eval(input('enter a valid weight'))
print('the weight of the object', weight/1000)