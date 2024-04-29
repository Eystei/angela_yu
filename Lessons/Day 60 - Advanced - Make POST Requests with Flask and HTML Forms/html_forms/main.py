from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    title = "Home"
    return render_template("index.html", title=title)


@app.route('/login_page', methods=["POST"])
def receive_data():
    name = request.form["username"]
    password = request.form["pass"]
    if not name or not password:
        return "<h1>Please fill all inputs with data !</h1>"
    return f"<h1>Name: {name}<br>Password: {password}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
