stu_names = {'Mike', 'John', 'Andrew', 'Alice'}
tut_name = {'John', 'Gerald', 'Don', 'Brian'}
print(stu_names | tut_name)
print(stu_names & tut_name)
sorted_names = sorted(tut_name)
print('the sorted names are', sorted_names)
joint_names = '-'.join(stu_names)
print('The joint names are', joint_names)


def countif(my_list, condition):
    return len([i for i in my_list if eval(condition)])


l = [56, 2, 4, 67, 87]
print(countif(l, 'i > 5'))

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# making an item to be an iterable


class Numbers:
    def __iter__(self):
        self.a = 1
        return self.a

    def __next__(self):
        if self.a < 15:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


# my_class = Numbers()
# my_l = iter(my_class)

# for x in my_l:
#   print(x)

# enumerate function- prints out the index position and the corresponding tuple element as well
my_tuple2 = ("apple", "banana", "cherry", 'mango')
for (i, x) in enumerate(my_tuple2):
    print(i+1, x)

# zip function
names = ['Mike', 'Brian', 'Mary', 'Kevin']
score = (65, 67, 62, 64)
merged_list = zip(names, score)
merge2 = dict(merged_list)
print(merge2)
for (i, x) in enumerate(merge2):
    print(i+1, x)

# list version
# print(list(merged_list))

from random import shuffle

# create the encryption key
alphabet = 'abcdefghijklmnopqrstuvwxyz'
L = list(alphabet)
print((shuffle(L)))

# making our dictionary using maketrans to create a special kind of dictionary that
# defines how things will be translated.

# encoding script
encode_dict = str.maketrans(dict(zip(alphabet, L)))
print(encode_dict)
trans_word = 'This is a secret'.translate(encode_dict)
print('The encoded form of the message is ', trans_word, sep='\n')

# decoding script
decode_dict = str.maketrans(dict(zip(L, alphabet)))
print(decode_dict)
exact_st = trans_word.translate(decode_dict)
print('The decoded form of the message is ', exact_st, sep='\n')


