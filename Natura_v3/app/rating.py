from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from app.models import User, places, ratings
from flask_login import current_user, login_user
from datetime import datetime

def save_user_rating(user_rating, name):
    place_id = db.session.query(places.id).filter(places.name==name)
    #STAVFEL I TABELL SKA VARA PLACEID
    save_rating_to_db = ratings(userid=current_user.id, placeid=place_id, ratings=user_rating, datetime=datetime.utcnow())
    db.session.add(save_rating_to_db)
    db.session.commit()
    return flash('Du har gett betyg.')

def average_rating():
    pass