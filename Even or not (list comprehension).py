import random
numlist = []
list = random.randint(1, 20)

while len(numlist) < list:
    numlist.append(random.randint(5, 100))
evenumlist = [number for number in numlist if number % 2 == 0]

print (numlist)
print (evenumlist)