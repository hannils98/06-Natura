from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from flask_login import current_user, login_user
from app.models import User, places, user_images
from werkzeug.urls import url_parse
from datetime import datetime
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os

dropzone = Dropzone(app)

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/app/static/uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app) # set maximum file size, default is 16MB


def image_upload(placeid):
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls'] # moved it one tab, fix so x doesnt show when uploading
    # handle image upload from Dropzone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f) 
            # save the file with to our photo folder
            filename = photos.save(file, name=file.filename)
            # append image urls
            file_urls.append(photos.url(filename))
            # save to database
            date = datetime.utcnow()
            image = user_images(userid=current_user.id, placeid=placeid, imageid=filename, datetime=date)
            db.session.add(image)
            db.session.commit()
        session['file_urls'] = file_urls
        return "Laddar upp..."
        
def remove_image(image_id):
    image = db.session.query(user_images).filter(user_images.userid==current_user.id, user_images.imageid==image_id).all()
    os.remove('app/static/uploads/' + image_id) 
    for i in image:
        db.session.delete(i)  
        db.session.commit()     
    return flash('Din bild har tagits bort!')