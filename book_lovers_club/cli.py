# cli.py
import click
from sqlalchemy.orm import Session
from models import Book, Genre
from database import engine, SessionLocal

@click.group()
def cli():
    pass

@cli.command()
@click.option('--title', prompt='Title', help='Book title.')
@click.option('--author', prompt='Author', help='Book author.')
@click.option('--rating', prompt='Rating', help='Book rating.', type=int)
@click.option('--review', prompt='Review', help='Book review.')
@click.option('--genre_id', prompt='Genre ID', help='ID of the genre.', type=int)
def add_book(title, author, rating, review, genre_id):
    with SessionLocal() as session:
        book = Book(title=title, author=author, rating=rating, review=review, genre_id=genre_id)
        session.add(book)
        session.commit()
        click.echo(f'Book "{title}" added.')

@cli.command()
def list_books():
    with SessionLocal() as session:
        books = session.query(Book).all()
        for book in books:
            click.echo(f"{book.title} by {book.author}, Rating: {book.rating}")

if __name__ == '__main__':
    cli()


