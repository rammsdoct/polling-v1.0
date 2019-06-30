from datetime import datetime
from flask import render_template
from flaskjob import app

@app.route('/')
@app.route('/home')
@app.route('/about')

def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "index.html",
        title = "Hello Flask",
        message = "Hello, Flask!",
        content = " on " + formatted_now)
def about():
    return render_template(
        "about.html",
        title = "About polling-1.1",
        content = "Example-autotest.")