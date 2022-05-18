from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_app import app
import uuid as uuid



@app.route('/display/project',methods=["POST","GET"])
def display_project():

    return render_template('display_project.html', images=Image.get_all_images())