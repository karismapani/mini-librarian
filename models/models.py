from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date
class Book(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    title:str
    author:str
    genre:str
    available:bool=True
class User(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
    email:str
class Borrow(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    user_id:int=Field(foreign_key="user.id")
    book_id:int=Field(foreign_key="book.id")
    borrowed_on:date=Field(default=date.today())
    returned_on:Optional[date]=None