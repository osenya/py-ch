count1 = 0
count2 = 0

for i in range(5):
    x = eval(input('enter a number '))
    if x % 2 == 0:
        count1 += 1
    else:
        count2 += 1
print('there are', count1, 'even numbers and', count2, 'odd numbers')


for i in range(5, 0, -1):
    print(i,' ', end='' ) # the end statement ensures the next statement printed is within the same line
print('we won the game')

# program that prints numbers and their square
for i in range(21):
    print('the square of ', i, 'is','---', i*i)

for i in range(5,0, -1):
    print('*' * i)

for i in range(0, 5):
    print('*' * i)

for i in range(0, 8, 2):
    print(' '*(3-i), '*' * (i+1), ' '*(3-i))