def init_board():
    board = [["x", ".", "."], [".", ".", "."], [".", ".", "x"]]
    return board


def get_move(board):
    letters = {'a': 0, 'b': 1, 'c': 2}
    numbers = {'1': 0, '2': 1, '3': 2}
    coordinates = ()
    while True:

        move = input("What's your move? ")
        row = move[0]
        col = move[1]
        if len(move) == 2:
            if row.isalpha() and col.isdigit():
                if row.lower() in letters.keys() and col in numbers.keys():
                    if board[letters[row.lower()]][numbers[col]] == '.':
                        coordinates = (letters[row.lower()], numbers[col])
                        break
                    else:
                        print("That place is already taken!")
                        continue
                else:
                    print("Letter should be from 'abc', number should be from '123'!")
                    continue
            else:
                print("Input must be one letter and one number!")
                continue
        else:
            print("Coordinate must have length of 2!")
            continue
    return coordinates



    

    


def mark(board, player):
    coordinates = get_move(board)
    board[coordinates[0]][coordinates[1]] = player
    return board




def has_won(board):
    colsfor0 = []
    colsforx = []

    #row win
    for row in board:
        if len(set(row)) == 1 and row[0] != '.':
            return True
        for i in range(len(row)):
            if row[i] == 'x':
                colsforx.append(i)
        for i in range(len(row)):
            if row[i] == '0':
                colsfor0.append(i)

    for x in colsforx:
        if colsforx.count(x) == 3:
            return True
    for x in colsfor0:
        if colsfor0.count(x) == 3:
            return True
    if board[0][0] == board[1][1] == board[2][2] != '.':
        return True

    elif board[0][2] == board[1][1] == board[2][0] != '.':
        return True

    return False

def is_full(board):
    board = init_board()
    count = []
    for row in board:
        count.append(row.count('.'))
    return count == [0, 0, 0]

    


def print_board(board):
    letters = ("A", "B", "C")
    print('  1', '  2', '  3')
    i = 0
    for row in board:
        print(letters[i], row[0], '|', row[1], '|', row[2])
        if i == 2:
            break
        print(' ---+---+---')
        i += 1
    print("\n")

   

def print_result(player, board):
    if has_won(board):
        print(player, "has won!")
    elif is_full(board):
        print("It's a tie")
    
def new_game():
    a = input("Do you want to play again? (y/n) ")
    return a.lower()
    
    
def tic_tac_toe():
    board = init_board()
    print_board(board)
    while True:
        player = 'x'
        mark(board, player)
        print_board(board)
        if has_won(board) or is_full(board):
            print_result(player, board)
            if new_game() == 'y':
                tic_tac_toe()
            else:
                print("Ciao!")
                return False
        
        player = '0'
        mark(board, player)
        print_board(board)
        if has_won(board) or is_full(board):
            print_result(player, board)
            if new_game() == 'y':
                tic_tac_toe()
            else:
                print("Ciao!")
                return False
             
            
tic_tac_toe()
