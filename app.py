from flask import Flask, render_template, request
import game as ga

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    ga.start_board = [[2, 2, 4, 4], [0, 4, 2, 2], [0, 2, 2, 0], [0, 2, 0, 2]]
    return render_template('main.html', board=ga.start_board, continue_game=True)


@app.route('/move')
def move():
    chosen_direction = request.args.get('direction', None)
    if chosen_direction == "left":
        ga.merge_left(ga.start_board)
    elif chosen_direction == "right":
        ga.merge_right(ga.start_board)
    elif chosen_direction == "up":
        ga.merge_up(ga.start_board)
    elif chosen_direction == "down":
        ga.merge_down(ga.start_board)

    add = ga.random_spawn(ga.start_board)

    if add is False:
        continue_game = False
        return render_template('main.html', gameover="Game over!", board=ga.start_board, continue_game=continue_game)

    continue_game = True
    return render_template('main.html', board=ga.start_board, continue_game=continue_game)


if __name__ == "__main__":
    app.run()