from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from app.models import User, places, ratings
from flask_login import current_user, login_user
from datetime import datetime
from sqlalchemy import exc, func

def show_user_rating(place_id):
    try:
        # We assume that rating is always unique per user and place
        saved_user_rating = db.session.query(ratings.ratings).filter(ratings.userid==current_user.id, ratings.placeid==place_id).scalar()
        
        return saved_user_rating
    except UnboundLocalError:
        return None  

def show_average_rating(place_id):
    try:
        avg = db.session.query(func.avg(ratings.ratings)).filter(ratings.placeid==place_id).scalar()
        return round(avg, 1)
    except UnboundLocalError: # This may obsolete when using scalar and not returning avg without setting 
        return None
    except TypeError: # This catches when it is not possible to calculate average(no ratings exist for a place) 
        return 'kan inte beräknas än'
    

def save_user_rating(user_rating, place_id):
    try:
        save_rating_to_db = ratings(userid=current_user.id, placeid=place_id, ratings=user_rating, datetime=datetime.utcnow())
        db.session.add(save_rating_to_db)
        db.session.commit()
        return flash('Du har gett betyg.')
    except exc.IntegrityError:
        db.session.rollback()
        return flash('Du har redan gett betyg för denna plats!')


