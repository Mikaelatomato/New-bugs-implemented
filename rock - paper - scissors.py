player1 = str(input("Name of the first player: "))
botornot = str(input("Play against a bot (player vs bot) y/n :  "))
while True:
    if botornot != "y" and botornot != "n":
        print("Invalid input")
        continue
    if botornot == "y":
        player2 = "bot"
        import random
    else:
        player2 = str(input("name of the second player: "))
        print("rock, paper or scissors?: ")
    game_dict = {"rock": 1, "paper": 2, "scissors": 3}
    while player1:
        player1pick = str(input("is turn for the player 1 to pick: "))
        if player1pick != "rock" and player1pick != "paper" and player1pick != "scissors":
            print("Invalid input")
            continue
        else:
            p1 = game_dict.get(player1pick)
            break
    if botornot == "y":
        botpick = random.choice(list(game_dict))
        p2 = game_dict.get(botpick)
    else:
        while player2:
            player2pick = str(input("is turn for the player 2 to pick: "))
            if player2pick != "rock" and player2pick != "paper" and player2pick != "scissors":
                print("Invalid input")
                continue
            else:
                p2 = game_dict.get(player2pick)
                break                
    dif = p1 - p2
    if dif in [0]:
        if botornot == "y":
            print ("the bot pick was: ", botpick)
        print("game: draw")
    elif dif in [1, -2]:
        if botornot == "y":
            print("the bot pick was: ", botpick)
        print(player1, " wins")
    elif dif in [2, -1]:
        if botornot == "y":
            print("the bot pick was: ", botpick)
        print(player2, " wins")
    stay = str(input("keep playing? y/n:  "))
    if stay == "y":
        continue
    else:
        print("thanks for playing :)")
        break