from flask import Flask
from flask import render_template
from flask import request
import random
import string
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", randomDiscNumber=random.randint(1, 100))

@app.route('/report')
def report():
    return render_template("report.html")

@app.route('/logs')
def logs():
    with open("data/saved_posts.txt", "r") as file:
        findings = {}
        for line in file.readlines():
            data = line.split(",")
            findings[data[0]] = [data[1], f"{data[2]} found disc #{data[3]} at {data[4]}"]
        print(findings)
    return render_template('logs.html', data=findings)


def generateRandomID():
    out = ""
    for i in range(5):
        out += random.choice(string.ascii_lowercase)
    return out

@app.route('/submit/', methods=["GET", "POST"])
def submit_form():
    if request.method == "GET":
        return "<h1>IDK what ur doing, you should be submitting a POST request to this, how did you 'GET' here?"

    if request.method == "POST":
        form_data = request.form

        for element in form_data:
            if form_data[element] == '':
                return render_template('report.html', message=f"Please enter a value for {element}")

        today = datetime.today()
        date = today.strftime("%m/%d/%Y")
        formatted_data = f"{generateRandomID()},{date},{form_data['name']},{form_data['discnum']},{form_data['location']}\n"
        print(formatted_data)
        with open('data/saved_posts.txt', 'a') as outfile:
            outfile.write(formatted_data)
        return render_template('submit.html', data=formatted_data)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/join')
def join():
    return render_template('join.html')


if __name__ == '__main__':
    app.run()
