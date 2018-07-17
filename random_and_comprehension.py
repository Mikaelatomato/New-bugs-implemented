import random
from random import randint
random_len = list(range(1, randint(10, 20)+1))  # i use this list to determinate a random len
random_len2 = list(range(1, randint(10, 20)+1))
a = random.sample(range(100), len(random_len))
b = random.sample(range(100), len(random_len2))
d = set([number for number in a if number in b])  # list comprehension done in with line using the set class.
print(a)
print(b)
if not d:           # if the list is empty
    print("there aren't common items")
else:
    print(d)
