from flask import Flask, render_template, request
import game as ga
import copy

app = Flask(__name__)
score = 0

@app.route('/')
@app.route('/main')
def main():
    ga.start_board = [[2, 2, 4, 4], [0, 4, 2, 2], [0, 2, 2, 0], [0, 2, 0, 2]]
    global score
    score = 0
    return render_template('main.html', board=ga.start_board, continue_game=True, score=score)


@app.route('/move')
def move():
    global score
    chosen_direction = request.args.get('direction', None)
    actual_board = copy.deepcopy(ga.start_board)

    if chosen_direction == "left":
        ga.merge_left(ga.start_board)
    elif chosen_direction == "right":
        ga.merge_right(ga.start_board)
    elif chosen_direction == "up":
        ga.merge_up(ga.start_board)
    elif chosen_direction == "down":
        ga.merge_down(ga.start_board)

    if actual_board != ga.start_board:
        score += 10
        add = ga.random_spawn(ga.start_board)
    else:
        add = True

    if add is False:
        continue_game = False
        return render_template('main.html', gameover="Game over!", board=ga.start_board, continue_game=continue_game, score=score)

    continue_game = True
    return render_template('main.html', board=ga.start_board, continue_game=continue_game, score=score)


if __name__ == "__main__":
    app.run()