from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_app import app
import uuid as uuid
from flask_app.models.project import Project
from flask_app.models.stored_html import Elements
# image proccessing
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'avif'])
UPLOAD_FOLDER = 'flask_app/static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1080 * 1554
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# ---------------------------------------


@app.route('/display/project/<int:project_id>',methods=["POST","GET"])
def display_project(project_id):
    data={
        'id':project_id}
    project=Project.get_project(data)
    print(project.name)

    return render_template('display_project.html', navbar = Elements.navbars(), project=project)

@app.route('/display/all_projects',methods=["POST","GET"])
def display_projects():
    projects= Project.all_projects()
    return render_template('all_projects.html', projects=projects, navbar = Elements.navbars())

@app.route('/create/project',methods=["POST","GET"])
def create_project():

    return render_template('create_project.html', navbar = Elements.navbars())

@app.route('/create/project/query', methods=['POST'])
def query_create_proeject():
    files = request.files.getlist('files[]')
    for file in files:
        file=secure_filename(file.filename)
        if len(file)<1:
            data={
            'name' : request.form['name'],
            'description' : request.form['description'],
            'image' : 'default_project.png',
            }
            Project.create_project(data)
        else:
            files = request.files.getlist('files[]')
            print(files, "hello")
            pic_name=''
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    pic_name = str(uuid.uuid1()) + "_" + filename
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
                    print(pic_name,'pic_name', filename, file)
            data={
                'name' : request.form['name'],
                'description' : request.form['description'],
                'image' : pic_name,
            }
            Project.create_project(data)
    return redirect(request.referrer)