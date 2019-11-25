from application import app, db
from flask import render_template, request, redirect, url_for

from application.books.models import Book
from application.books.forms import BookForm


@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books=Book.query.all())


@app.route("/books/new/")
def books_form():
    form = BookForm()
    return render_template("books/new.html", form=form)


@app.route("/books/", methods=["POST"])
def books_create():
    form = BookForm(request.form)

    print('------------------------------')

    if form.validate_on_submit():
        print('---------------HAHAA!')
        newBook = Book(form.name.data, form.author.data, form.description.data)
        db.session().add(newBook)
        db.session().commit()
        return redirect(url_for("books_index"))

    return render_template("books/new.html", form=form)


@app.route("/books/<book_id>/", methods=["GET", "POST"])
def books_contact(book_id):
    if "update" in request.form:
        return redirect(url_for("books_update", book_id=book_id))
    else:
        return redirect(url_for("books_index"))


@app.route("/books/update/<book_id>/", methods=["GET", "POST"])
def books_update(book_id):
    book = Book.query.get(book_id)
    form = BookForm(obj=book)

    if form.validate_on_submit():
        form.populate_obj(book)
        db.session().commit()
        return redirect(url_for("books_index"))

    return render_template("books/update.html", book=book, form=form)
