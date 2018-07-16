import random
count = 0
user1 = 0
stay = str
listran = range(1,10)
number = random.randint(1, 9)
while True:
    user1 = int(input(("Try to guess a number between 1 and 9: ")))
    if user1 not in listran:
        print("invalid input")
        continue
    else:
        if user1 < number:
            print("aim higher")
            count += 1
            continue
        elif user1 > number:
            print("aim lower")
            count += 1
            continue
        if user1 == number:
            print("naisu, you did it in ", count, " attempts")
        stay = input("Wanna keep playing? y/n = ")
        number = random.randint(1, 9) #number and count are also here, so everytime the user plays again, it picks a new random number and the counter is reset.
        count = 0
        while stay != "y" and stay != "n":
            print("invalid input")
        if stay == "y":
            continue
    if stay == "n":
        break