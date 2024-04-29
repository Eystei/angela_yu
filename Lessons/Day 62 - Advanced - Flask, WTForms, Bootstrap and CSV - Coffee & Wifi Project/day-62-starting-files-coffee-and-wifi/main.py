from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(
        label='Cafe name',
        validators=[DataRequired()])
    location = StringField(
        label='Cafe location on Google Maps (URL)',
        validators=[DataRequired(), URL()])
    open = StringField(
        label="Opening Time e.g. 8AM",
        validators=[DataRequired()])
    close = StringField(
        label='Closing Time e.g. 5:30PM',
        validators=[DataRequired()])
    coffee_rating = SelectField(
        label='Coffee Rating',
        choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
        validators=[DataRequired()])
    wifi_rating = SelectField(
        label='Wifi Strength Rating',
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()])
    power_rating = SelectField(
        label='Power Socket Availability',
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(file='cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
            csv_file.write(
                f"\n{form.cafe.data},"
                f"{form.location.data},"
                f"{form.open.data},"
                f"{form.close.data},"
                f"{form.coffee_rating.data},"
                f"{form.wifi_rating.data},"
                f"{form.power_rating.data}"
            )
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
