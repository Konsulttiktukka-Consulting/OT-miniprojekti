from flask import Flask, request, render_template, url_for
from application import app

@app.route("/")
def fronPage():
    return render_template('frontpage.html')
