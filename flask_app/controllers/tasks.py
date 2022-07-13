from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_app import app
import uuid as uuid
from flask_app.models.stored_html import Elements

@app.route('/display/tasks',methods=["POST","GET"])
def display_tasks():

    return render_template('open_tasks.html', navbar = Elements.navbars())