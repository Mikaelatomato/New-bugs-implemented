if __name__ == "__main__":
    import random
    count = 1
    list = list(range(1,102))
    print ("Think on a number between 1 and 100, and i'll try to guess it, but don't lie to me, you fucking baka!\n")

def guessing():
    count = 1
    userchoice = int
    end_index = 100
    start_index = 0
    while userchoice != "1" or end_index <= 100 or start_index >= 0:
        dif = end_index - start_index
        botpick = random.choice(list[start_index : end_index ])
        print("\n\nis",botpick, "the number that you are thinking, a-anon?")
        userchoice = input("\n1. yes owo / 2. no, aim 'higher' / 3. no, aim 'lower' : ")
        if userchoice == "2":
            count += 1
            start_index = botpick
        elif userchoice == "3":
            count += 1
            end_index = botpick - 1
        if userchoice == "1":
            return print("\n\nI knew it and it only took me",count,"attempt(s), but isn't like a know you or a-a-anything...")
        if userchoice != "1" and userchoice != "2" and userchoice != "3":
            print ("\ni don't like your jokes anon!!")
            break
        if dif == 1:
            print ("\n it must be fucking",botpick,"stop playing with me!!")
            break
        if start_index == 100 and end_index == 100:
            print("\n it must be fucking",botpick, "stop playing with me!!")
            break

guessing()
