import random
import copy


def generate_start_board():
    random_x, random_y = random.randint(0, 3), random.randint(0, 3)
    random_x2, random_y2 = random.randint(0, 3), random.randint(0, 3)
    print(random_x, random_y)
    print(random_x2, random_y2)
    board = [4 * [0] for _ in range(4)]
    board[random_x][random_y], board[random_x2][random_y2] = 2, 2

    return board


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


def check_if_game_is_over(board):
    if 0 in [elem for sublist in board for elem in sublist]:
        return False
    board_copy = copy.deepcopy(board)
    merge_left(board_copy), merge_right(board_copy), merge_down(board_copy), merge_down(board_copy)
    if board_copy == board:
        return True
    return False

