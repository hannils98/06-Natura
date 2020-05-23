from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from app.models import User, places, ratings, user_images, Symbol, PlaceHasSymbol
from flask_login import current_user, login_user
from datetime import datetime
from sqlalchemy import exc, func
from flask import jsonify

def get_symbols_for_place(place_id):
     return [str(symbol) for symbol in db.session.query(PlaceHasSymbol.symbol_id).filter(PlaceHasSymbol.place_id==place_id).all()]