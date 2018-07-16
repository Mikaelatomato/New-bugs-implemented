import random
a = random.sample(range(1, 50), 20)
b = random.sample(range(10, 50), 20)
print(a, b)
commonlist = []
for element in a:
    for element2 in b:
        if element == element2:
            if element not in commonlist:
                commonlist.append(element)
if not commonlist:
    print("there aren't common items")
else:
    print(commonlist)