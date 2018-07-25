print ("Welcome, ladies and gentleman to the hangman game\nYou already know what the game is about so all i'm telling you is that\nYou can try to guess 6 times, and you need the sowpodes dic to play.")
def main():
    def pickaword():
        import random
        with open('sowpods.txt', 'r') as f :
            list2 = list(f)
            word = random.choice(list2)
            return word.strip("\n")

    def hangman():
        global count2
        triesleft = 6 - count2
        print("  +=====+          ")
        print("  |     '")
        if count2 >= 1:
            print("  |     O           ")
        else:
            print("  |                  You have",  triesleft, "tries left")
        if count2 == 6:
            print("  |    /|\            You have",  triesleft, "tries left") 
        elif count2 == 5:                   # Credits to khdc-me for this func (https://github.com/khdc-me)
            print("  |    /|              You have",  triesleft, "tries left") #  i'm too lazy and it would be the same at the end.
        elif count2 >= 2:
            print("  |     |               You have",  triesleft, "tries left")
        else:
            print("  |                      ")
        if count2 >= 4:
            print("  |    / \\")
        elif count2 == 3:
            print("  |    /")
        else:
            print("  |")
        print("  |")
        print("==========")

    def game(word):
        import re
        global lost
        global wins
        count = 0
        global count2
        usedwords = []
        board = ["_"] * len(word)
        word2 = list(word)
        while "_" in board and count < 6:
            hangman()
            print ("\n")
            print (board)
            while True:
                userguess = input("\nTry to guess a letter (must be uppercase): ")
                if not re.match("[A-Z]", userguess):
                    print ("\nOnly UPPERCASE letters allowed")
                    continue
                elif userguess in usedwords:
                    print("\nYou have already used the letter: ", userguess)
                    continue
                elif len(userguess) > 1:
                    print ("\nYou can only guess 1 letter at the time, you dumb fuck.")
                    continue
                elif userguess not in usedwords:
                    usedwords.append(userguess)
                    break
            if userguess not in word2:
                print ("\nLooks like this letter isn't in the word.")
                count += 1
                count2 += 1
                continue
            while userguess in word2:
                    board[word2.index(userguess)] = userguess
                    word2[word2.index(userguess)] = "Guessed"
        if count <= 5:
            wins += 1
            hangman()
            print ("\n")
            print (word, "!!!!")
            print ("\nCongratulations Shinji, With this you have: ", wins, "/", lost, "- wins/loses\n")
        if count == 6:
            lost += 1
            hangman()
            print ("\n")
            print ("The word was: ", word, "!!!, you are a baka >:c\nWith this you have: ", wins, "/", lost, "- wins/loses\n")
    game(pickaword())

    def playagain():
        global count2
        while True:
            play = input("Wanna play again? (Y/N): ")
            if play != "y" and play != "Y" and play != "n" and play != "N":
                print ("invalid input")
                continue
            if play == "y" or play == "Y":
                count2 = 0
                main()
            if play == "n" or play == "N":
                exit()
    playagain()

if __name__ == "__main__":
    count2 = 0
    lost = 0
    wins = 0
    main()
