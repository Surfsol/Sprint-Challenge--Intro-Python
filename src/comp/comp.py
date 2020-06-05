# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
a = [str(item).split(':')[1].split(',')[0][1:] for item in humans if 'D' in str(item)]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [str(item).split()[1][:-1] for item in humans if 'e,' in str(item)]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [str(item).split()[1][:-1] for item in humans if str(item).split()[1][0] in ['C','D','E','F','G']]
print(c)

import re
# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [int(re.sub("[^0-9]","", str(age))) + 10 for age in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [str(item).split()[1][:-1] + '-' + str(re.sub("[^0-9]","", str(item))) for item in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(str(item).split()[1][:-1], int(re.sub("[^0-9]","", str(item)))) for item in humans if 27 <= int(re.sub("[^0-9]","", str(item))) <= 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(str(item).split()[1][:-1].upper(), int(re.sub("[^0-9]","", str(item))) + 5) for item in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(int(re.sub("[^0-9]","", str(age)))) for age in humans]
print(h)
