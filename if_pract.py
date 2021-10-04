correct_num = 7
count = 0
guess = eval(input('enter you number'))

if guess == correct_num:
    print('you win the game')
if not(guess == correct_num):
    print('you entered the wrong value, try again')
    count = count + 1
    print(count)

# a program to check if a number is prime through a flag condition
num = eval(input('enter a number'))
flag = 0
for i in range(2, num):
    if num % i == 0:  # dividing the number
        flag = 1

if flag == 1:
    print('the number is not a prime')
else:
    print('the number is a prime')


largest = eval(input('enter any positive number'))

for i in range(3):
    num = eval(input('enter positive number'))
    if num>largest:
        largest = num

print('the largest number is', largest)

s = 0
for i in range(10):
 num = eval(input('Enter a number: '))
 s = s + num
print('The average is', s/10)
