from flask import Flask, render_template
import requests

posts_json = requests.get("https://api.npoint.io/b0f99cd01aed6121481d").json()

flask = Flask(__name__)


@flask.route("/")
def home():
    header_title = "Home"
    return render_template("index.html", title=header_title, posts_json=posts_json)


@flask.route("/about")
def about():
    header_title = "About Me"
    return render_template("about.html", title=header_title)


@flask.route("/contact")
def contact():
    header_title = "Contacts"
    return render_template("contact.html", title=header_title)


@flask.route("/post/<int:index>")
def show_post(index):
    for post in posts_json:
        if post["id"] == index:
            return render_template("post.html", post=post)
    return "Sorry 404"


if __name__ == '__main__':
    flask.run(debug=True)
