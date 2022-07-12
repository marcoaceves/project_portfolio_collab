from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_app.models.stored_html import Elements
from flask_app import app
import uuid as uuid

@app.route('/')
def index():
    navbar = Elements.navbars()
    print(navbar, "$$$")
    print("helo")

    return render_template('index.html', navbar=navbar)