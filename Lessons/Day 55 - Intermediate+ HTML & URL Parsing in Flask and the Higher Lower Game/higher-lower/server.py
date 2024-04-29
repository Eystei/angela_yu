from flask import Flask
from random import randint
from style_decorators import make_bold, make_italic

flask = Flask(__name__)

@flask.route("/")
@make_italic
@make_bold
def home_page():
    return """
        <h1 style="text-align: center">Guess a number between 0 and 9</h1>
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">
    """


rand_number = randint(0, 9)


@flask.route("/<int:guess>")
def guess_number(guess):
    if guess > rand_number:
        return """
        <h1 style='color: purple'>Too high, try again!</h1>
        <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>
        """

    if guess < rand_number:
        return """
        <h1 style='color: red'>Too low, try again!</h1>
        <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>
        """

    return """
        <h1 style='color: green'>You found me!</h1>
        <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>
    """


if __name__ == '__main__':
    flask.run(debug=True)
