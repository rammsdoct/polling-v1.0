from flask import Flask
from flaskjob import app

@app.route('/')
@app.route('/home')
def home():
    return "Flask is running!"
