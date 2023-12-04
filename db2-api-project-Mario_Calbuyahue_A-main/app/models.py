from datetime import date, datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    isbn: Mapped[str] = mapped_column(index=True)
    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str]
    year: Mapped[int]
    language: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: "Mapped[Author]" = relationship(back_populates="books")
    categories: "Mapped[list[Category]]" = relationship(
        back_populates="books", secondary="books_categories"
    )


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    biography: Mapped[Optional[str]]
    date_of_birth: Mapped[Optional[date]]

    books: "Mapped[list[Book]]" = relationship(back_populates="author")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    books: "Mapped[list[Book]]" = relationship(
        back_populates="categories", secondary="books_categories"
    )


class BookCategory(Base):
    __tablename__ = "books_categories"

    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), primary_key=True)


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class BookCopy(Base):
    __tablename__ = "book_copies"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    status: Mapped[str] = mapped_column()


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_copy_id: Mapped[int] = mapped_column(ForeignKey("book_copies.id"))
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    loaned_date: Mapped[datetime] = mapped_column()
    return_date: Mapped[datetime] = mapped_column()
    returned_date: Mapped[datetime] = mapped_column()
    penalty: Mapped[int] = mapped_column()
