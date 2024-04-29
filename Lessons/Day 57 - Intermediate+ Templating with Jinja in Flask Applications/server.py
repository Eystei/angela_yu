from flask import Flask, render_template
from datetime import datetime
import random
import requests

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, current_year=current_year)


@app.route("/guess/<name>")
def guess_page(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_json = requests.get(f"https://api.agify.io?name={name}").json()
    age = age_json["age"]

    return render_template("guess.html", person_name=name, gender=gender, age=age)


@app.route("/blog/<index>")
def get_blog(index):
    blog_url = "https://api.npoint.io/aa26813bd0cbb46ec2f8"
    blog_response = requests.get(blog_url)
    blog_all_posts = blog_response.json()
    return render_template("blog.html", posts=blog_all_posts)


if __name__ == "__main__":
    app.run(debug=True)
