def main():
    print ("Welcome, morons and bakas, to The Tic Tac Toe Game\n\nThe first player to get 3 consecutive 'x'(in player 1 case) or 'o'(in player 2 case) wins\nTo selec a block, write the cords like this: row,colum \nfor example: 1,3 , that's all, gl bakas\n")
    def newgame():
        board_size = 3
        for i in range(board_size):
            print(" ---- " * (board_size))
            print("| xo |" * (board_size))
            print(" ---- " * board_size)
        new_game = [['-', '-', '-'],
                    ['-', '-', '-'],
                    ['-', '-', '-']]
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
                    if new_game[0][i] == new_game[1][i] == new_game[2][i] and new_game[i][i] != '-': #vertical check
                        if new_game[i][i] == 'X':
                            return 1
                        else:
                            return 2
                    if new_game[i][0] == new_game[i][1] == new_game[i][2] and new_game[i][i] != '-': # horizontal check
                        if new_game[i][i] == 'X':
                            return 1
                        else:
                            return 2
                if new_game[0][0] == new_game[1][1] == new_game[2][2] and new_game[1][1] != '-': #diag check 1
                    if new_game[1][1] == 'X':
                        return 1
                    else:
                        return 2
                if new_game[0][2] == new_game[1][1] == new_game[2][0] and new_game[1][1] != '-': #diag check 2
                    if new_game[1][1] == 'X':
                        return 1
                    else:
                        return 2
        def playing(winner):
            winner1 = winner
            count = 0
            while  winner1 == None:
                if count == 9:
                    print("DRAW!!!")
                    winner1 = 3
                    return winner1
                playerturn1 = 0
                playerturn2 = 0
                while playerturn1 == 0 and winner1 == None and count < 9:
                    while True:
                        try:
                            player1_move = input("\nWrite the coordinates for 'X': ")
                            x = int(player1_move[0])
                            y = int(player1_move[2])
                            player1coordinates = player1_move.strip().split(",")
                            row = int(player1coordinates[0]) - 1
                            col = int(player1coordinates[1]) - 1
                            break
                        except ValueError:
                            print ("Invalid coordinates, the must be typed as: row,col\nWithing a range from 1 to 3\nfor example: 1,3")
                        except IndexError:
                            print ("Invalid coordinates, the must be typed as: row,col\nWithing a range from 1 to 3\nfor example: 1,3")
                    if x > 3 or x <= 0 or y > 3 or y <= 0:
                        print ("Coordinates out of range, the range must be from 1 to 3")
                        continue
                    if new_game[row][col] == '-':
                        new_game[row][col] = 'X'
                        count += 1
                        playerturn1 = 1
                        drawboard(new_game)
                        winner1 = whoiswinner()
                     else:
                        print ("This place is already taken")
                        continue
                while playerturn2 == 0 and winner1 == None and count < 9:
                    while True:
                        try:
                            player2_move = input("\nWrite the coordinates for 'O': ")
                            x = int(player2_move[0])
                            y = int(player2_move[2])
                            player2coordinates = player2_move.strip().split(",")
                            row = int(player2coordinates[0]) - 1
                            col = int(player2coordinates[1]) - 1
                            break
                        except ValueError:
                            print ("Invalid coordinates, the must be typed as: row,col\nWithing a range from 1 to 3\nfor example: 1,3")
                        except IndexError:
                            print ("Invalid coordinates, the must be typed as: row,col\nWithing a range from 1 to 3\nfor example: 1,3")
                    if x > 3 or x <= 0 or y > 3 or y <= 0:
                        print ("Coordinates out of range, the range must be from 1 to 3")
                        continue
                    if new_game[row][col] == '-':
                        new_game[row][col] = 'O'
                        count += 1
                        playerturn2 = 1
                        drawboard(new_game)
                        winner1 = whoiswinner()
                    else:
                        print ("This place is already taken")
                        continue
            if winner1 == 1:
                print ("Player 1 wins!!!\n")
                return (winner1)
            elif winner1 == 2:
                print ("Player 2 wins!!!\n")
                return (winner1)

        def play(winner1):
            if winner1 == 1:
               global player1count
               player1count += 1
            elif winner1 == 2:
                global player2count
                player2count += 1
            elif winner1 == 3:
                global drawcount
                drawcount += 1
        play(playing(whoiswinner()))

        print("Player1 has won: ", player1count,
              "times,\nPlayer2 has won: ", player2count,
              "times,\nAnd you have a total of: ", drawcount, "draws")
        while True:
            answer = input('\nPlay Again? (y/n): ')
            if answer != 'y' and answer != 'n':
                print ("invalid input")
                continue
            if answer == 'n':
                print ("\nThanks for playing baka!")
                exit()
            if answer == 'y':
                newgame()
    newgame()

if __name__ == "__main__":
    player1count = 0
    player2count = 0
    drawcount = 0
    main()
