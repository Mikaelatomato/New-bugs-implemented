def main():
    print ("Welcome, morons and bakas, to The Tic Tac Toe Game\n\nThe first player that gets 3 consecutive 'x'(in player 1 case) or 'o'(in player 2 case) wins\nTo selec a block, write the cords like this: row,colum \nfor example: 1,3 , that's all, gl bakas\n")
    board_size = 3
    for i in range(board_size):
        print(" --- " * board_size)
        print("|   |" * (board_size))
        print(" --- " * board_size)
    new_game = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

    def drawboard(board):
        print('---------------')
        print('|    |   |    |')
        print('| ' + str(board[0][0]) + '  | ' + str(board[0][1]) + ' |  ' + str(board[0][2]) + ' |')
        print('|    |   |    |')
        print('---------------')
        print('|    |   |    |')
        print('| ' + str(board[1][0]) + '  | ' + str(board[1][1]) + ' |  ' + str(board[1][2]) + ' |')  # a better ver of Sreekaanth91 but the credit is for him
        print('|    |   |    |')
        print('---------------')
        print('|    |   |    |')
        print('| ' + str(board[2][0]) + '  | ' + str(board[2][1]) + ' |  ' + str(board[2][2]) + ' |')
        print('|    |   |    |')
        print('---------------')

    def whoiswinner():
            for i in range(len(new_game)):
                if new_game[0][i] == new_game[1][i] == new_game[2][i] and new_game[i][i] != 0: #vertical check
                    if new_game[i][i] == 1:
                        return 1
                    else:
                        return 2
                if new_game[i][0] == new_game[i][1] == new_game[i][2] and new_game[i][i] != 0: # horizontal check
                    if new_game[i][i] == 1:
                        return 1
                    else:
                        return 2
            if new_game[0][0] == new_game[1][1] == new_game[2][2] and new_game[1][1] != 0: #diag check 1
                if new_game[1][1] == 1:
                    return 1
                else:
                    return 2
            if new_game[0][2] == new_game[1][1] == new_game[2][0] and new_game[1][1] != 0: #diag check 2
                if new_game[1][1] == 1:
                    return 1
                else:
                    return 2

    def playing(winner):
        winner1 = winner
        while  winner1 == None:
            playerturn1 = 0
            playerturn2 = 0
            while playerturn1 == 0 and winner1 == None:
                player1_move =input("\nWrite the coordinates for 'X': ")
                player1coordinates = player1_move.strip().split(",")
                row = int(player1coordinates[0]) - 1
                col = int(player1coordinates[1]) - 1
                if new_game[row][col] == 0:
                    new_game[row][col] = 1
                    playerturn1 = 1
                    drawboard(new_game)
                    winner1 = whoiswinner()
                else:
                    print("This place is already taken")
                    continue
            while playerturn2 == 0 and winner1 == None:
                player2_move = input("\nWrite the coordinates for 'O': ")
                player2coordinates = player2_move.strip().split(",")
                row = int(player2coordinates[0]) - 1
                col = int(player2coordinates[1]) - 1
                if new_game[row][col] == 0:
                    new_game[row][col] = 2
                    playerturn2 = 1
                    drawboard(new_game)
                    winner1 = whoiswinner()
                else:
                    print ("This place is already taken")
                    continue
        if winner1 == 1:
            print ("Player 1 wins")
        elif winner1 == 2:
            print ("Player 2 wins")

    playing(whoiswinner())

    while True:
            answer = input('Run again? (y/n): ')
            if answer != 'y' and answer != 'n':
                print ("invalid input")
                continue
            if answer == 'n':
                break
            if answer == 'y':
                main()

if __name__ == "__main__":
    main()
