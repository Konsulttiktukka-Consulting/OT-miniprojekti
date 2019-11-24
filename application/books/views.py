from application import app,db
from flask import render_template, request, redirect, url_for

from application.books.models import Book
from application.books.forms import BookForm

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

@app.route("/books/<book_id>/", methods=["GET", "POST"])
def books_contact(book_id):
    if "update" in request.form:
        return books_update(book_id)
    else:
        return redirect(url_for("books_index"))
                        
@app.route("/books/update/<book_id>/", methods=["GET", "POST"])
def books_update(book_id):
    book = Book.query.get(book_id)
    form = BookForm(obj=book)

    if form.validate_on_submit():
        form.populate_obj(book)
        db.session().commit()
                
    return render_template("books/update.html", book=book, form=form)


