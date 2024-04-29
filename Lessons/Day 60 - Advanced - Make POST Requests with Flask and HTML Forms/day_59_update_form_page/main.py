from flask import Flask, render_template, request
import requests
import smtplib

my_email = "buzinov.yura@gmail.com"
subject = "Day 60 - Advanced - Make POST Requests with Flask and HTML Forms"
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


@flask.route("/contact", methods=["POST", "GET"])
def contact():
    header_title = "Contacts"
    if request.method == "POST":
        text = "Successfully sent message"
        data = request.form

        send_email(data['name'], data['email'], data['phone_number'], data['message'])

        return render_template("contact.html", text=text, title=header_title)
    return render_template("contact.html", text="Contact Me", title=header_title)


@flask.route("/post/<int:index>")
def show_post(index):
    for post in posts_json:
        if post["id"] == index:
            return render_template("post.html", post=post)
    return "Sorry 404"


def send_email(name, email, phone, message):
    email_message = f"Subject:Day 60 - Advanced - Make POST Requests with Flask and HTML Forms\n\n" \
                    f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password="lcgy eebc gcvp vmus")
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=email_message
        )


if __name__ == '__main__':
    flask.run(debug=True)
