from flask import render_template
from app.email import send_email

def email_book_list(user, recipient_email, books):
    send_email('Someone has shared their Book Center list with you!',
    sender = user.email,
    recipients=[recipient_email], 
    text_body=render_template('email/email_list.txt', user=user, books=books),
    html_body=render_template('email/email_list.html', user=user, books=books))