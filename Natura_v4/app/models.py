import os
from datetime import datetime
import jwt
from sqlalchemy import Sequence, create_engine, Column, Integer, String, event
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry, exc
from app import db, app, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from time import time
from hashlib import md5


followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id',ondelete="CASCADE")),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"))
)
Base = declarative_base()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author',cascade="all, delete", passive_deletes=True, lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
            self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                                algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"),)

    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class places(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer,primary_key=True )
    name = db.Column( db.Text)
    description= db.Column(db.Text)
    source = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

class is_in(db.Model):
    __tablename__ ='is_in'
    place_id= db.Column(db.Integer, db.ForeignKey('places.id'),primary_key=True)
    sub_place_id= db.Column(db.Integer, db.ForeignKey('places.id'), primary_key=True)

class categories(db.Model):
    __tablename__='categories'
    name= db.Column(db.Text)
    id= db.Column(db.Integer, primary_key=True)


class place_has_cat(db.Model):
    __tablename__ = 'place_has_cat'
    cat_id= db.Column(db.Integer,db.ForeignKey('categories.id'), primary_key=True)
    place_id= db.Column(db.Integer, db.ForeignKey('places.id'), primary_key=True)

class ratings(db.Model):
    __tablename__ = 'ratings'
    userid= db.Column(db.Integer, db.ForeignKey('user.id',ondelete="CASCADE"), primary_key=True)
    placeid=db.Column(db.Integer, db.ForeignKey('places.id'), primary_key=True)
    ratings=db.Column(db.Integer)
    datetime=db.Column(db.DateTime(timezone=True))


class user_images(db.Model):
    __tablename__ = 'user_images'
    userid= db.Column(db.Integer,Sequence('user_images_seq'), db.ForeignKey('user.id',ondelete="CASCADE") ,primary_key=True)
    placeid=db.Column(db.Integer, db.ForeignKey('places.id'))
    alt=db.Column(db.Text)
    imageid=db.Column(db.Text, primary_key=True)
    description=db.Column(db.Text)
    datetime=db.Column(db.DateTime(timezone=True))

class admin_images(db.Model):
    __tablename__ = 'admin_images'
    placeid= db.Column(db.Integer,db.ForeignKey('places.id'))
    alt= db.Column(db.Text)
    imageid= db.Column(db.Text, primary_key=True)
    description= db.Column(db.Text)
    datetime= db.Column(db.DateTime(timezone=True))


db_url = 'postgresql://ak2195:l6kp3gsl@pgserver.mah.se/natura_v2'
engine = create_engine(db_url, echo=True)
@event.listens_for(engine, "connect")
def connect(dbapi_connection, connection_record):
    connection_record.info['pid'] = os.getpid()

@event.listens_for(engine, "checkout")
def checkout(dbapi_connection, connection_record, connection_proxy):
    pid = os.getpid()
    if connection_record.info['pid'] != pid:
        connection_record.connection = connection_proxy.connection = None
        raise exc.DisconnectionError(
                "Connection record belongs to pid %s, "
                "attempting to check out in pid %s" %
                (connection_record.info['pid'], pid)
        )
Base.metadata.create_all(engine)