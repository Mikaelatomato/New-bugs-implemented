leave = str
while leave != "exit":
    num = int(input("Give me a number sir: ")) #idk how to ask for a number again if the user doesn't put one (if he doesn't, the code wil end in a exception)
    numlist = [i for i in range(2, num) if num % i == 0] #doesn't start from 1, since a prime number can be divided by itself but also by 1
    def primeornot():
        if not (numlist):
            return print("is prime")
        else:
            return print("isn't prime")
    primeornot()
    while leave:
        leave = input("type 'exit' or 'continue': ")
        if leave != "exit" and leave != "continue":
            print("invalid input")
            continue
        else:
            break
