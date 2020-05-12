from app.models import user_images
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required

def get_user_images(placeid):
    images_list = []
    images = db.session.query(user_images.alt).filter(user_images.placeid==placeid)
    for image in images:
        for a in image:
            images_list.append(a)
    return images_list

def get_all_images():
    images_list = []
    images = db.session.query(user_images.alt)
    for image in images:
        for a in image:
            images_list.append(a)
    return images_list

def get_my_images():
    images_list = []
    images = db.session.query(user_images.imageid).filter(user_images.userid==current_user.id).all()
    print(images)
    for image in images:
        for a in image:
            images_list.append(a)
    return images_list
