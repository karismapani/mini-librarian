from sqlmodel import Session,select
from models.models import Book
class BookService:
    def create_book(self,session,data):
        book=Book(
            title=data.title,
            author=data.author,
            genre=data.genre
        )
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    def get_allbook(self,session):
        books=session.exec(select(Book)).all()
        return books
    def get_book(self, session, id):
        book = session.get(Book, id)
        return book
    def delete_book(self, session, id):
        book = session.get(Book, id)
        session.delete(book)
        session.commit()
        return {"message": "Book deleted!"}