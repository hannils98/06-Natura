from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from app.models import User, places, ratings
from flask_login import current_user, login_user
from datetime import datetime
from sqlalchemy import exc
from flask import jsonify

def show_user_rating(name):
    try:
        saved_user_rating = db.session.query(ratings.ratings).join(places).filter(ratings.userid==current_user.id, places.name==name)
        for i in saved_user_rating:
            for j in i:
                user_rating = j
        return j
    except UnboundLocalError:
        return None      

def save_user_rating(user_rating, name):
    try:
        place_id = db.session.query(places.id).filter(places.name==name)
        save_rating_to_db = ratings(userid=current_user.id, placeid=place_id, ratings=user_rating, datetime=datetime.utcnow())
        db.session.add(save_rating_to_db)
        db.session.commit()
        return flash('Du har gett betyg.')
    except exc.IntegrityError:
        db.session.rollback()
        return flash('Du har redan gett betyg för denna plats!')


def average_rating():
    pass