from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from book import Book, Review, SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def create_book(title: str, author: str, publication_year: int, db: Session = Depends(get_db)):
    new_book = Book(title=title, author=author, publication_year=publication_year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.post("/books/add_review")
def submit_review(title: str, text_review: str, rating: int, db: Session = Depends(get_db)):
    new_review = Review(title=title, text_review=text_review, rating=rating)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

@app.post("/books/get_review")
def get_review(title: str, db: Session = Depends(get_db)):
    query = db.query(Review)
    query = query.filter(Review.title == title)
    reviews = query.all()
    return reviews

@app.get("/get_books/")
def get_all_books(author: str = None, publication_year: int = None, db: Session = Depends(get_db)):
    query = db.query(Book)

    if author:
        query = query.filter(Book.author == author)
    if publication_year:
        query = query.filter(Book.publication_year == publication_year)

    books = query.all()
    return books