import pytest
from application.books.models import Book


def test_testi(db_session):
    print("testi")
    book = Book("Testi","Testi","Testi")
    response = db_session().add(book)

##Parametrit on määritelty conftest.py filussa.
# Huom db_session ja _db on eri
def test_save_request(_db):
    print("testi1")
    book = Book("Testi","Testi","Testi")
    response = _db.session().add(book)
    _db.session().commit()
    result = _db.session().execute('select * from book;')
    for row in result:
        print(row)
    assert(1==2)