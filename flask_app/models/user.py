from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt =Bcrypt(app)


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")


db ='project_manager_db'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.image = data['image']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, image,  email, password) VALUES (%(first_name)s, %(last_name)s,%(image)s,%(email)s, %(password)s);'
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update_profile(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, image=%(image)s WHERE id =%(id)s "
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_by_email(cls, data):
        query ="SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(db).query_db(query, data)
        if len(result)< 1 :
            return False
        print(result)
        return cls(result[0])
    @classmethod
    def get_user(cls, data):
        query = "SELECT first_name, last_name, image, email, created_at, updated_at, id FROM users WHERE id = %(id)s"
        result = connectToMySQL(db).query_db(query, data)
        print(result)
        result[0]['password'] = ''
        return cls(result[0])

    @staticmethod
    def validate_user( user ):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query,user)
        query = "SELECT * FROM users WHERE user_name = %(user_name)s;"
        resultsUsername = connectToMySQL(db).query_db(query,user)
        # test whether a field matches the pattern
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if len(resultsUsername) >= 1:
            flash("User Name is already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if not PASS_REGEX.match(user['password']):
            flash("Password must contain at least 8 characters, 1 Uppercase, 1 Lowercase, 1 Number","register")
            is_valid=False
        if len(user['user_name']) < 3:
            flash("User name must be at least 3 characters","register")
            is_valid= False

        if user['password'] != user['confirm_password']:
            flash("Passwords don't match","register")
        return is_valid
