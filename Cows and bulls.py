import random
if __name__ == '__main__':
    play = True
    numberguess = str(random.randint(1000, 9999))
    attempts = 0
    print ("WELCOME TO Cows and Bulls, \n i'm to generate a random 4 digit number, and YOU'll HAVE TO GUESS IT, \n that's right, for each digit in the place you get 1 cow,\n and for each digit in the wrong place you get 1 bull. \n If you get 4 cows you win. I-i-isn't like a want you to play but,\n you can leave whenever you want typing 'exit'")

def userguess():
    while True:
        userguess = input("Try to guess a 4 digit number: ")
        if len(userguess) != 4:
            print ("it must be a 4 digit number, you moron!")
            continue
        elif userguess == "exit":
            exit()
        else:
            break
    return userguess

def compare(numberguess, userguess):
    cowsbulls = [0, 0]
    for i in range(len(numberguess)):
        if numberguess[i] == userguess[i]:
            cowsbulls[0] += 1
        elif numberguess[i] in userguess:
            cowsbulls[1] += 1
    return cowsbulls

while play:
    cowsbullscount = compare(numberguess, userguess())
    if cowsbullscount[0] == 4:
        print ("Congratulations Shinji, omedeto, you have won! it only took you ", attempts, "attempts")
        stay = input("Wanna play again? Y / WHATEVER: ")
        if stay == "Y" or "y":
            numberguess = str(random.randint(1000, 9999))
            attempts = 0
            continue
        else:
            break
    else:
        print ("Wrong!, for now you have ", cowsbullscount[0], "cows and ", cowsbullscount[1], "bulls")
        attempts += 1
