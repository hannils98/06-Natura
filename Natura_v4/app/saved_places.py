from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from app.models import User, SavedPlace
from flask_login import current_user, login_user
from datetime import datetime
from sqlalchemy import exc, func

def saved_place(placeid):
    lst = []
    saved = db.session.query(SavedPlace).filter_by(placeid=placeid, userid=current_user.id)
    for s in saved:
        lst.append(s)
    if len(lst) == 0:
        return False
    else:
        return True

def save_place(placeid):
    try:
        save_place = SavedPlace(placeid=placeid, userid=current_user.id, datetime=datetime.utcnow())
        db.session.add(save_place)
        db.session.commit()
        return flash('Du har nu sparat platsen!')
    except exc.IntegrityError:
        db.session.rollback()
        return flash('Du har redan sparat platsen!')

def unsave_place(place_id):
    place = db.session.query(SavedPlace).filter_by(placeid=place_id, userid=current_user.id)
    for p in place:
        db.session.delete(p)  
        db.session.commit()     
    return flash('Platsen är inte längre sparad!')
