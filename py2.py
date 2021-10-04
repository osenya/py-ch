
# practise on lists
from random import choice
from random import shuffle
from random import sample
countries = ["kenya","Uganda", "Tz", "DRC"]
citizens = ["Kenyan", "Ugandan", "Tanzanian", "congolese"]
print(countries[-3])
print(countries[1:3])
# elements can be replaced directly on the list
countries[1] = "Rwanda"
# printing all elements after the element in the index position 1
print(countries[1:])
if "Kenya" in countries:
    print("your list contains the country searched")

# list functions
# merging two lists
countries.extend(citizens)
print(countries)

# adding sthng to a list at the end
citizens.append("Rwandese")

# add at a specific location
citizens.insert(2, "Zambian")
print(citizens)

# remove something from the list
countries.remove("DRC")
print(countries)

# listname.clear clears all the element in t6he list

# pop function
countries.pop()
print(countries)

# to check if an element is in the list
print(countries.index("Ugandan"))

# counting the number of times an element appears in the list
print(countries.count("DRC"))

# sorting items in a list
citizens.reverse()
print(citizens)

# finding the number of items
print(len(citizens))
# copying elements
citizens2 = citizens.copy()
shuffle(citizens)
print(citizens)

# sum(listname) finds the sum of the numbers in the list
# min(listname) finds the minimum number  in the list items
# max(listname) finds the minimum number in the list

fav_country = choice(countries)
print(fav_country)
fav_citizens = sample(citizens, 2)
print(fav_citizens)
# sample(listname, 2) samples two elements from the list.

