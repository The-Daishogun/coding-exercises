def generate_board():
    return {7: "1", 8: "2", 9: "3", 4: "4", 5: "5", 6: "6", 1: "7", 2: "8", 3: "9"}


def get_input(player):
    if player == 1:
        pstr = "Player one"
    else:
        pstr = "Player two"

    return input("{0}'s turn! Input the cell you want:\n".format(pstr))


def set_cell_value(cell, player, board):
    if player == 1:
        value = "x"
    else:
        value = "o"

    board[int(cell)] = value


def get_cell_value(cell, board):
    return board[int(cell)]


def check_win(board):
    for i in range(1, 4, 3):
        if board[i] == board[i + 1] == board [i + 2]:
            return board[i], True
    for i in range(1, 4):
        if board[i] == board[i + 3] == board [i + 6]:
            return board[i], True
    if board[1] == board[5] == board[9]:
        return board[1], True
    elif board[3] == board[5] == board[7]:
        return board[3], True
    else:
        return "", False


def generate_row(row_num, board):
    row = "|"
    if row_num == 1:
        start = 1
        finish = 4
    elif row_num == 3:
        start = 4
        finish = 7
    else:
        start = 7
        finish = 10

    for column in range(start, finish):
        row += get_cell_value(column, board)+"|"
    return row


def generate_divider():
    return "-------"


def print_board(board):
    for row in range(1, 6):
        if row == 1 or row == 3 or row == 5:
            print(generate_row(row, board))
        else:
            print(generate_divider())


def end_game(test):
    if test[0] == "x":
        pstr = "Player One"
    else:
        pstr = "player Two"
    return "{0} Is The Winner!!!".format(pstr), False


def check_tie(board):
    counter = 0
    for key in board:
        if board[key] == "x":
            counter += 1
    if counter == 5:
        return True
    else:
        return False


print("Welcome!\nPlayer one is X and Player 2 is O")

board = generate_board()
print_board(board)
move_along = True

while move_along:

    p_one = get_input(1)
    set_cell_value(p_one, 1, board)
    print_board(board)
    test = check_win(board)
    if test[1]:
        end_condition = end_game(test)
        print(end_condition[0])
        move_along = end_condition[1]
        break
    if check_tie(board):
        print("It's a TIE!")
        move_along = False
        break

    p_two = get_input(2)
    set_cell_value(p_two, 2, board)
    print_board(board)
    test = check_win(board)
    if test[1]:
        end_condition = end_game(test)
        print(end_condition[0])
        move_along = end_condition[1]
        break
