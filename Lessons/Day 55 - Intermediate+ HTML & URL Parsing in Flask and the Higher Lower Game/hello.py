from flask import Flask
import style_decorators

flask = Flask(__name__)


@flask.route("/")
def hello_world():
    return """
        <style>
            img {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 500;
            }
            
            p {
                text-align: center;
            }
        </style>
        
        <h3><p>Hello, World!</p></h3>
        <h4><p>This is a simple paragraph</p></h4>
        <img src='https://compote.slate.com/images/2f2fc6b0-96b7-4bf7-812a-dcaa8c6ce3d6.gif'>
    """


@flask.route("/lorem")
@style_decorators.make_italic
@style_decorators.make_bold
@style_decorators.make_underline
@style_decorators.center_text
def lorem():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur laoreet lacinia " \
           "risus ac convallis. "


@flask.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello guys ! {name} you're on the <code>{number} first page!!!</code>"


if __name__ == '__main__':
    flask.run(debug=True)
