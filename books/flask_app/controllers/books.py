from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/books')
def books():
    return render_template('books.html', all_books=Book.get_all())

@app.route('/create/books', methods=['POST'])
def create_books():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    book_id = Book.save(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_book(id):
    data = {
        'id': id
    }
    return render_template('show_book.html', book=Book.get_by_id(data), unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/join/author', methods=['POST'])
def join_author():
    join_author_only = Author.add_favorite(request.form)
    data = {
        'author_id': ['author_id'],
        'book_id': ['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/books/{request.form['book_id']}")
    