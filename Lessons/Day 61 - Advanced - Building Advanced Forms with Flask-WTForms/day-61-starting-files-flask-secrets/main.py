from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(
        label='Email:',
        validators=[
            DataRequired(),
            Email("you must type a valid email (with '@' and '.'')")
        ])
    password = PasswordField(
        label='Password:',
        validators=[
            DataRequired(),
            Length(min=8, message='you must type at least 8 characters.')
        ])
    submit = SubmitField(label='Log IN')


app = Flask(__name__)
app.secret_key = "Secret key"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "1234567890":
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
