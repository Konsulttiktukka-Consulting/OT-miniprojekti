from flask import Flask, request, render_template, url_for
from application import app

@app.route("/")
def frontPage():
    return render_template('index.html')
