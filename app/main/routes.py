from flask import render_template, url_for, redirect, flash
from flask_login import login_required, current_user
from app import db
from app.main import bp
from app.main.forms import BookForm, ShareBookListForm
from app.models import Book
from app.main.email import email_book_list

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    books = current_user.books
    return render_template('index.html', title='Home', books=books)
    
@bp.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, date_purchased=form.date_purchased.data, notes=form.notes.data, user=current_user)
        db.session.add(book)
        db.session.commit()
        flash('Book added to your library.')
        return redirect(url_for('main.index'))
        
    return render_template('book/add_book.html', title='Add Book', form=form)
    
@bp.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    if book:
        form = BookForm(obj=book)
    else:
        return redirect(url_for('main.index'))
    
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = author=form.author.data
        book.date_purchased = date_purchased=form.date_purchased.data
        book.notes = notes=form.notes.data
        db.session.add(book)
        db.session.commit()
        flash('Book updated.')
        return redirect(url_for('main.index'))  
           
    return render_template('book/edit_book.html', title='Edit Book', form=form)


@bp.route('/send_book_list', methods=['GET', 'POST'])  
@login_required
def send_book_list():
    form = ShareBookListForm()
    if form.validate_on_submit():
        books = current_user.books
        email_book_list(current_user, form.email.data, books)
        flash('Book list sent.')
        return redirect(url_for('main.index'))
    return render_template('book/send_books.html', title='Share Books', form=form)
