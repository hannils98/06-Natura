from threading import Thread
from flask import render_template
from flask_mail import Message
from app import app, mail
from app.forms import ContactForm


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Natura] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))

def contact_email(email):
    form = ContactForm()
    email = form.email.data
    message = form.message.data
    subject = form.subject.data
    send_email(subject,
               sender=email,
               recipients=app.config['ADMINS'][0],
               text_body=render_template('email/mail.txt',
                                         email=email, message=message, subject=subject),
               html_body=render_template('email/mail.html', email=email, message=message, subject=subject))