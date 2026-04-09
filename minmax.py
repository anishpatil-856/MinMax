
board = [' ' for _ in range(9)]   # 3x3 tic-tac-toe board represented as a list


def print_board():
    print()                     #prints empty line for spacing 
    print(board[0] + " | " + board[1] + " | " + board[2])   #1 st row is printed here 
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])       # 2 nd row is printed here
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])       #3 rd row is printed here 
    print()


def check_winner(player):                                   #winning condition is checked here 
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],   # rows
        [0,3,6],[1,4,7],[2,5,8],   # columns
        [0,4,8],[2,4,6]            # diagonals
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:     # to check if all these position have the same mark . 
            return True
    return False


def is_full():
    return ' ' not in board      # a function to check if the board is full or not . if there is no empty space then it returns true otherwise false . 


def minimax(is_max):

    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_full():
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                if score > best:
                    best = score
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                if score < best:
                    best = score
        return best


def best_move():
    best_score = -100
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move



while True:
    print_board()

    # Player move
    pos = int(input("Enter position (0-8): "))
    if board[pos] == ' ':
        board[pos] = 'X'
    else:
        print("Invalid move")
        continue

    if check_winner('X'):
        print_board()
        print("You Win!")
        break

    if is_full():
        print_board()
        print("Draw!")
        break


    ai_move = best_move()
    board[ai_move] = 'O'

    if check_winner('O'):
        print_board()
        print("AI Wins!")
        break

    if is_full():
        print_board()
        print("Draw!")
        break