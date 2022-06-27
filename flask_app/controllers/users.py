from flask import Flask, flash, request, redirect, session, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_bcrypt import Bcrypt
from flask_app import app
import uuid as uuid
from flask_app.models.user import User

bcrypt = Bcrypt(app)

# image proccessing
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'avif'])
UPLOAD_FOLDER = 'flask_app/static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1080 * 1554
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# -----------------------------------------------------------------


@app.route('/register',methods=["POST","GET"])
def display_registration():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('registration.html', images=Image.get_all_images())


@app.route('/register/query', methods=['POST'])
def query_registration():
    # if not User.validate_user(request.form):
    #     return redirect(request.referrer)
    # files = request.files.getlist('files[]')
    # print(files)
    # pic_name=''
    # for file in files:
    #     print("hello")
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         pic_name = str(uuid.uuid1()) + "_" + filename
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
    # print(pic_name,'pic_name')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data={
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'image' : 'default.png',
        'email' : request.form['email'],
        'password' : pw_hash,
        'confirm_password' : request.form['confirm_password'],
    }
    User.create_user(data)
    return redirect('/login')

@app.route('/login',methods=["POST","GET"])
def display_login():
    if 'user_id' in session:
        return redirect('/dashboard')

    return render_template('login.html', images=Image.get_all_images())
@app.route('/login/query', methods=['POST'])
def login():
    data={'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid Email or Password!', 'login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email or Password!', 'login')
        return redirect('/login')
    session['user_id']  = user_in_db.id

    return redirect ('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    data={'id':session["user_id"]}
    user=User.get_user(data)
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
