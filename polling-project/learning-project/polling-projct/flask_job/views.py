from flask import Flask
from flask_job import app

@app.route('/')
@app.route('/home')
def home():
    return "Flask Running!"
