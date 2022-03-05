from flask import Flask
from flask import render_template
from flask import request
import random
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
        findings = file.readlines()
    return render_template('logs.html', data=findings)

@app.route('/submit/', methods=["GET", "POST"])
def submit_form():
    if request.method == "GET":
        return "<h1>IDK what ur doing, you should be submitting a POST request to this, how did you 'GET' here?"
    if request.method == "POST":
        form_data = request.form
        formatted_data = f"{form_data['name']} found disc #{form_data['discnum']} at {form_data['location']}\n"
        print(formatted_data)
        with open('data/saved_posts.txt', 'a') as outfile:
            outfile.write(formatted_data)
        return render_template('submit.html', data=formatted_data)


if __name__ == '__main__':
    app.run()
