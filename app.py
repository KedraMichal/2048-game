from flask import Flask, render_template, request, url_for
import game as ga
import copy
import threading
import time
import keyboard


app = Flask(__name__)
score = 0


@app.route('/')
@app.route('/main')
def main():
    global score
    score = 0
    global board
    board = ga.generate_start_board()

    return render_template('main.html', board=board, continue_game=False, score=score)


@app.route('/move')
def move():
    if ga.check_if_game_is_over(board) is True:
        return render_template('main.html', board=board, continue_game=False, score=score, gameover="Game over!")

    return render_template('main.html', board=board, continue_game=True, score=score)


def key_press_handler():
    global score
    while True:
        while True:
            try:
                if keyboard.is_pressed('a'):
                    chosen_direction = 'left'
                    break
                elif keyboard.is_pressed('w'):
                    chosen_direction = 'up'
                    break
                elif keyboard.is_pressed('s'):
                    chosen_direction = "down"
                    break
                elif keyboard.is_pressed('d'):
                    chosen_direction = "right"
                    break
            except:
                pass

        actual_board = copy.deepcopy(board)
        if chosen_direction == "left":
            ga.merge_left(board)
        elif chosen_direction == "right":
            ga.merge_right(board)
        elif chosen_direction == "up":
            ga.merge_up(board)
        elif chosen_direction == "down":
            ga.merge_down(board)

        if actual_board != board:
            score += 10
            ga.random_spawn(board)
            time.sleep(0.4)


if __name__ == "__main__":
    thread1 = threading.Thread(target=key_press_handler)
    thread2 = threading.Thread(target=app.run)
    thread1.start()
    thread2.start()

