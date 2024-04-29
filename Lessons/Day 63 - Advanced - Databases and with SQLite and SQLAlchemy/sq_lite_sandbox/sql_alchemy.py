from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}'


with app.app_context():
    db.create_all()

# CREATE A NEW RECORD
with app.app_context():
    new_book = Book(title="Harry Potter 5", author="J.K.Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
# NOTE: When creating new records, the primary key fields is optional. you can also write:
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)

# READ ALL RECORDS
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()

# READ A PARTICULAR RECORD BY QUERY
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter 2")).scalar()
    print(book)

# UPDATE A PARTICULAR RECORD BY QUERY
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == 'Harry Potter 2')).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# UPDATE A RECORD BY PRIMARY KEY
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == 2)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()
# FLASK-SQLALCHEMY ALSO HAS SOME HANDY EXTRA QUERY METHODS LIKE GET_OR_404()
# THAT WE CAN USE. SINCE FLASK-SQLALCHEMY VERSION 3.0 THE PREVIOUS QUERY METHODS
# LIKE BOOK.QUERY.GET() HAVE BEEN DEPRECATED

# DELETE A PARTICULAR RECORD BY PRIMARY KEY
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == 4)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

# YOU CAN ALSO DELETE BY QUERYING FOR A PARTICULAR VALUE E.G. BY TITLE OR
# ONE OF THE OTHER PROPERTIES. AGAIN, THE GET_OR_404() METHOD IS QUITE HANDY.
