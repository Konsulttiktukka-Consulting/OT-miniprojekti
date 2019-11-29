from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from application import db
from application.books.models import Book
from application.books.forms import BookForm
from sqlalchemy import text

bp = Blueprint("books", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/books", methods=["GET"])
def books_index():
    sql = text('''
    SELECT id, title, category FROM Video 
    UNION 
    SELECT id, title, category FROM Book''')
    result = db.engine.execute(sql)

    return render_template("books/list.html", data=result)


@bp.route("/books/new/")
def books_form():
    form = BookForm()
    return render_template("books/new.html", form=form)


@bp.route("/books/", methods=["GET", "POST"])
def books_create():
    form = BookForm(request.form)
    if form.validate_on_submit():
        newBook = Book(form.title.data, form.author.data,
                       form.description.data)
        db.session().add(newBook)
        db.session().commit()
        return redirect(url_for("books.books_index"))

    return render_template("books/new.html", form=form)


@bp.route("/books/<book_id>/", methods=["GET", "POST"])
def books_contact(book_id):
    if "update" in request.form:
        return redirect(url_for("books.books_update", book_id=book_id))
    else:
        return redirect(url_for("books.books_index"))


@bp.route("/books/update/<book_id>/", methods=["GET", "POST"])
def books_update(book_id):
    book = Book.query.get(book_id)
    form = BookForm(obj=book)

    if form.validate_on_submit():
        form.populate_obj(book)
        db.session().commit()
        return redirect(url_for("books.books_index"))

    return render_template("books/update.html", book=book, form=form)
