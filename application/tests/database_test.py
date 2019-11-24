import pytest
from application.books.models import Book



def test_new_book_can_be_added(_db):
    testParameters = ["NewName","NewAuthor","GoodBook"]
    book = Book(testParameters[0], testParameters[1],testParameters[2])
    response = _db.session().add(book)
    _db.session().commit()

    result = _db.session().execute('select * from book;')
    for row in result:
        assert(row.name == testParameters[0])
        assert(row.author== testParameters[1])
        assert(row.description == testParameters[2])

def test_invalid_book_cant_be_added(_db):
    testParameters = ["NewName","NewAuthor","GoodBook"]
    request = "INSERT INTO book (name, description) VALUES('NewName','GoodBook')"
    with pytest.raises(Exception) as e:
       assert _db.session().execute(request)
    assert("IntegrityError" in str(e)  )
