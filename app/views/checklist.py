from app import app, db

import requests

from datetime import date
from flask import render_template,redirect, url_for, flash, request
from app.models import Book, Member, Transaction, Book_borrowed

# Renders transaction page
@app.route('/transactions')
def transactions_page():
    # reads all transactions
    transaction = Transaction.query.order_by('id').all()
    books_to_borrow = Book.query.filter(Book.borrow_stock > 0).all()
    members_can_borrows = Member.query.filter(Member.to_pay < 500).all()
    books_to_return =  Book.query.filter(Book.borrower).all()
    return render_template('transactions/transactions.html', 
                            transactions = transaction, length=len(transaction), 
                            books_to_borrow = books_to_borrow, 
                            members_can_borrow = members_can_borrows, 
                            books_to_return = books_to_return)

