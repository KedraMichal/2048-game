import random


start_board = [[2, 2, 4, 4], [0, 4, 2, 2], [0, 2, 2, 0], [0, 2, 0, 2]]
print(start_board[2][1])


def display_board(board):
    for row in board:
        for value in row:
            print(value, end='|')
        print()


def move_to_left(board):
    for i in range(4):
        tmp = 0
        for j in range(3):
            if board[i][tmp] == 0:
                board[i].pop(tmp)
                board[i].append(0)
            else:
                tmp += 1


def merge_left(board):
    move_to_left(board)
    for j in range(4):
        for i in range(1):
            if board[j][i] == board[j][i + 1]:
                board[j][i] = 2 * board[j][i]
                if board[j][i + 2] == board[j][i + 3]:
                    board[j][i + 1] = 2 * board[j][i + 2]
                    board[j][i + 2], board[j][i + 3] = 0, 0
                    break
                else:
                    board[j][i + 1] = board[j][i + 2]
                    board[j][i + 2] = board[j][i + 3]
                    board[j][i + 3] = 0
                    break
            if board[j][i + 1] == board[j][i + 2]:
                board[j][i + 1] = 2 * board[j][i + 1]
                board[j][i + 2] = board[j][i + 3]
                board[j][i + 3] = 0
                break
            if board[j][i + 2] == board[j][i + 3]:
                board[j][i + 2] = 2 * board[j][i + 2]
                board[j][i + 3] = 0


def reverse_board(board):
    for row in board:
        row.reverse()


def transpose_board(board):
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            board[i][j], board[j][i] = board[j][i], board[i][j]


def merge_right(board):
    reverse_board(board)
    merge_left(board)
    reverse_board(board)


def merge_down(board):
    transpose_board(board)
    reverse_board(board)
    merge_left(board)
    reverse_board(board)
    transpose_board(board)


def merge_up(board):
    transpose_board(board)
    merge_left(board)
    transpose_board(board)


def random_spawn(board):
    places_with_null = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                places_with_null.append([i, j])

    if places_with_null:
        x, y = random.choice(places_with_null)
        board[x][y] = 2
    else:
        return False  # game over

def game(board):
    display_board(board)
    while True:
        move = input("w a s d ")
        if move == "w":
            merge_up(board)
            random_spawn(board)
            display_board(board)
        if move == "a":
            merge_left(board)
            random_spawn(board)
            display_board(board)
        if move == "s":
            merge_down(board)
            random_spawn(board)
            display_board(board)
        if move == "d":
            merge_right(board)
            random_spawn(board)
            display_board(board)


#game(start_board)