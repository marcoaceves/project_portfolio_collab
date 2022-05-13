from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_app import app
import uuid as uuid

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'flask_app/static/uploads' 
  

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=["POST","GET"])
def index():

    print( "TTTTTTTTTTTTTT")
    return render_template('index.html', images=Image.get_all_images())

@app.route("/upload",methods=["POST","GET"])
def upload():

    if request.method == 'POST':
        files = request.files.getlist('files[]')
        #print(files)
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                pic_name = str(uuid.uuid1()) + "_" + filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))


                data ={'filename': pic_name
                            }
            print(file)
            Image.upload_image(data)
        flash('File(s) successfully uploaded')
    return redirect('/')