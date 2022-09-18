from multiprocessing.sharedctypes import Value

def main():
    player1 = []
    player2 = []
    count = 0
    board = board_positions()
    while not alter_board == "X" and not alter_board == "O" and count < 9:
        print_board(board)
        print()
        position = input_move(count, player1, player2)
        if count % 2 == 0:
            player1.append(position)
        else:
            player2.append(position)
        board = alter_board(player1, player2)
        if(check_win(player1) == True):
            print_board(board)
            print("Player 1 has won!")
            break
        elif(check_win(player2) == True):
            print_board(board)
            print("Player 2 has won!")
            break
        count += 1
    
    if count == 9:
        print_board(board)
        print("Tie")


def board_positions():
    board = []
    row, column = 3, 3
    for i in range(row):
        for j in range(column):
            num = i*3 + j*1
            if j == 0:
                board_row = "| " + str(num) + " | "
            elif j == 1:
                board_row += str(num)
            else:
                board_row += " | " + str(num) + " |"
        board.append(board_row)
    return board

def print_board(board):
    print(board[0])
    print(board[1])
    print(board[2])

def input_move(count, player1, player2):
    if count % 2 == 0:
        while True:
            try:
                position = int(input("Player 1's turn. Input move (0-8): "))
                if position in player1 or position in player2 or position < 0 or position > 8:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid input")
                continue
    else:
        while True:
            try:
                position = int(input("Player 2's turn. Input move (0-8): "))
                if position in player1 or position in player2 or position < 0 or position > 8:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid input")
                continue

    return position

def alter_board(player1, player2):
    board = []
    row, column = 3, 3
    for i in range(row):
        for j in range(column):
            num = i*3 + j*1
            if num in player1:
                if j == 0:
                    board_row = "| " + "X" + " | "
                elif j == 1:
                    board_row += "X"
                else:
                    board_row += " | " + "X" + " |"
            elif num in player2:
                if j == 0:
                    board_row = "| " + "O" + " | "
                elif j == 1:
                    board_row += "O"
                else:
                    board_row += " | " + "O" + " |"
            else:
                if j == 0:
                    board_row = "| " + " " + " | "
                elif j == 1:
                    board_row += " "
                else:
                    board_row += " | " + " " + " |"
        board.append(board_row)

    return board

def check_win(player):
    if all(num in player for num in [0, 1, 2]) or all(num in player for num in [3, 4, 5]) or all(num in player for num in [6, 7, 8]):
        return True
    elif all(num in player for num in [0, 3, 6]) or all(num in player for num in [1, 4, 7]) or all(num in player for num in [2, 5, 8]):
        return True
    elif all(num in player for num in [0, 4, 8]) or all(num in player for num in [2, 4, 6]):
        return True
    
    return False

main()