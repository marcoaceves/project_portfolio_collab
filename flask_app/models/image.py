
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app import app
from datetime import datetime
import math
from flask import flash
import smtplib


db = 'upload_db'

class Image:
    def __init__(self, data):
        self.file_name = data['file_name']
        self.id = data['id']




    @classmethod
    def upload_image(cls,data):
        query = "INSERT INTO upload (file_name) VALUES (%(filename)s)"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_images(cls):
        query = "SELECT * FROM upload;"
        results = connectToMySQL(db).query_db(query)
        images = []
        for i in results:
            images.append( cls(i) )
        return images
