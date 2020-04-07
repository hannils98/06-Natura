from flask import Flask, render_template, request, redirect, url_for, flash, session
import psycopg2
import hashlib
from datetime import datetime
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os

app = Flask(__name__, static_url_path='/static')

dropzone = Dropzone(app)

conn = psycopg2.connect(dbname="natura", user="ak2195", password="l6kp3gsl", host="pgserver.mah.se")

cursor = conn.cursor()

app.config['SECRET_KEY'] = 'SVOqQTpAZETTTd-P8wqtpA'
loggedin = False
user = ""

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'gallery'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/static/uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app) # set maximum file size, default is 16MB

@app.route('/', methods=['GET'])
def index():
    
    global loggedin
    if request.args.get('welcome') and loggedin == False:
        return redirect('/login')
    elif request.args.get('accountcreated') and loggedin == False:
         return redirect('/login')
    user = request.args.get('welcome')
    newuser = request.args.get('accountcreated')
    loggedout = request.args.get('info')
    return render_template('index.html', user=user, newuser=newuser, loggedin=loggedin, loggedout=loggedout)

@app.route('/createaccount', methods=['GET'])
def createaccount():
    global loggedin 
    loggedin = False
    info = request.args.get('info')
    return render_template('createaccount.html', info=info, loggedin=loggedin)

@app.route('/creating', methods=['POST', 'GET'])
def creating():
    cursor = conn.cursor()

    try:
        if request.method == 'POST':
            email = request.form['email']
            username = request.form['username']
            password_1 = request.form['psw']
            password_2 = request.form['psw2']

            if password_1 == password_2:
                if len(password_1) >= 6:

                    t_hashed = hashlib.sha3_512(password_1.encode())
                    t_password = t_hashed.hexdigest()
                    dt = str(datetime.now())

                    cursor.execute("INSERT into userlogin VALUES ('" + username + "', '" + t_password + "', '" + email + "', '" + dt +"')")
                    conn.commit() 
                    global loggedin
                    loggedin = True
                    global user 
                    user = username

                    return redirect('/?accountcreated=' + username)
                else:
                    return redirect('/createaccount?info=Lösenordet är för kort')

            else: 
                return redirect('/createaccount?info=Du skrev inte in samma lösenord')
                
    except psycopg2.errors.UniqueViolation:
        return redirect('/createaccount?info=Användarnamnet eller emailen finns redan registrerad')

@app.route('/login', methods=['GET'])
def login():
    global loggedin
    loggedin = False
    info = request.args.get('info')
    return render_template('login.html', info=info, loggedin=loggedin)

@app.route('/loggingin', methods=['POST', 'GET'])
def loggingin():
    
    global user

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['psw']
        t_hashed = hashlib.sha3_512(password.encode())
        encr_password = t_hashed.hexdigest()

        try:
            cursor.execute("select username, password from userlogin where username='" + username + "' and password='" + encr_password + "'")
            
            users = []
            for record in cursor:
                users.append(record)

            for user in users:
                user = user[0]
            
            if len(users) > 0:
                global loggedin 
                loggedin = True

                return redirect('/?welcome=' + user)

            else:
                return redirect('/login?info=Var det rätt användarnamn och lösenord?')
        except UnboundLocalError or psycopg2.errors.InFailedSqlTransaction:
            return redirect('/login?info=Var det rätt användarnamn och lösenord?')

    else:
        return redirect('/login?info=Prova igen')

@app.route('/myaccount')
def myaccount():
    global user
    return render_template('myaccount.html', user=user)

@app.route('/logout')
def logout():
    global loggedin
    global user
    loggedin = False
    return redirect('/?info=Du är nu utloggad ' + user)

@app.route('/category')
def category():
    global loggedin

    return render_template('category.html', loggedin=loggedin)
    
@app.route('/category/<name>')
def subcat(name):
    global loggedin
    return render_template('category.html', loggedin=loggedin)
    

@app.route('/info')
def info():
    global loggedin
    return render_template('info.html', loggedin=loggedin)
    

@app.route('/contact')
def contact():
    global loggedin
    return render_template('contact.html', loggedin=loggedin)
    
@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    global loggedin
    if loggedin == True:
        # set session for image results
        if "file_urls" not in session:
            session['file_urls'] = []
        # list to hold our uploaded image urls
        file_urls = session['file_urls']

        # handle image upload from Dropzone
        if request.method == 'POST':
            file_obj = request.files
            for f in file_obj:
                file = request.files.get(f)
                # save the file with to our photo folder
                filename = photos.save(file, name=file.filename)

                # append image urls
                file_urls.append(photos.url(filename))

            session['file_urls'] = file_urls
            return "uploading..."
        files = os.listdir('static/uploads')
        return render_template('gallery.html', loggedin=loggedin, files=files)
    else:
        return redirect('/login?info=Du måste vara inloggad för att se galleri') 
    

if __name__ == "__main__":
   app.run(host='localhost', port=8080, debug=True)
