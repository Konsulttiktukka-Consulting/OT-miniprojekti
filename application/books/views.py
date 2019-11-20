from application import app,db
from flask import render_template, request, redirect, url_for
from application.books.models import Book

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new/")
def books_form():
    return render_template("books/new.html")

@app.route("/books/", methods=["POST"])
def books_create():
    newBook = Book(request.form.get("name"),request.form.get("author"), request.form.get("description"))
    
    db.session().add(newBook)
    db.session().commit()
    return redirect(url_for("books_index"))


