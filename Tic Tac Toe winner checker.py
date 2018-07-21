if  __name__ == '__main__':
    player1 = 1
    player2 = 2
    empty = 0
    new_game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
def whoiswinner():
    winner = int
    while winner != 0:
        for i in range(len(new_game)):
            if new_game[0][i] == new_game[1][i] == new_game[2][i] and new_game[i] != 0 and new_game[i][i] != 0: #vertical check
                if new_game[i][i] == 1:
                    winner = 1
                else:
                    winner = 2 #i might put the winner = 0 after this and change the while to a while winner == 0, so this won't stop checking till there's a winner.
            if new_game[i][0] == new_game[i][1] == new_game[i][2] and new_game[i][i] != 0: # horizontal check
                if new_game[i][i] == 1:
                    winner = 1
                else:
                    winner = 2
        if new_game[0][0] == new_game[1][1] == new_game[2][2] and new_game[1][1] != 0: #diag check 1
            if new_game[1][1] == 1:
                winner = 1
            else:
                winner = 2
        if new_game[0][2] == new_game[1][1] == new_game[2][0] and new_game[1][1] != 0: #diag check 2
            if new_game[1][1] == 1:
                winner = 1
            else:
                winner = 2
        if winner == 1:
            print ("Player 1 wins")
            break
        elif winner == 2:
            print ("Player 2 wins")
            break
        else:
            winner = 0
    if winner == 0:
        print("No one has won")
whoiswinner()
