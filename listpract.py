
from random import choice
from random import sample
names = ["John", "Mike", "Jose", "David", "George"]
places = ["Karen", "Hampshire", "Jersey", "Jersey", "Texas"]


fav_name = choice(names)
print(fav_name)

names.insert(2, "Titus")
print(names)

sampled_places = sample(places, 2)
print(sampled_places)

print(places.index("Jersey"))
print(places.count("Jersey"))
print(len(places))

# examples on set
# union
print({1, 2, 3} | {5, 6, 7})

# intersection
print({3, 7, 8, 9} & {5, 8, 10, 7})

# difference
print({3, 6, 8, 9} - {6, 8, 3, 11})

# symmetric difference
print({1, 2, 3} ^ {3, 4})

# an element of
print(3 in {1, 2, 3})

cl = {3, 5, 7, 8, 9}
# cl.add(5)
# cl.remove(8)

cl2 = {3, 5, 7}
cl2.issubset(cl)
cl.issuperset(cl2)
cl_final = sorted(cl2)
print(cl_final)

# the join method in python
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x_final = mySeparator.join(myDict)

print(x_final)

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)
# the '#' for the above case will act as our means of our separation
print(x)

