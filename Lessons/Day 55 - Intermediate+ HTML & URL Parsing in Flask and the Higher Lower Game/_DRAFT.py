from flask import Flask
from random import randint

server = Flask(__name__)

win_num = randint(0, 9)


@server.route('/')
def home_page():
    return "Hello, this is just a GAME"


@server.route('/<int:guess>')
def guess_number(guess):
    if guess > win_num:
        return "To High!"

    if guess < win_num:
        return "To Low!"

    return "You win"


if __name__ == '__main__':
    server.run(debug=True)
