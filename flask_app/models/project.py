from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt



db ='project_manager_db'

class Project:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_project(cls, data):
        query = 'INSERT INTO projects (name, description, image) VALUES (%(name)s, %(description)s,%(image)s);'
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update_project(cls,data):
        query = "UPDATE projects SET name=%(name)s, description=%(description)s, image=%(image)s WHERE id =%(id)s "
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_project(cls, data):
        query = "SELECT name, description, image, created_at, updated_at, id FROM projects WHERE id = %(id)s"
        result = connectToMySQL(db).query_db(query, data)
        print(result)
        return cls(result[0])

    @staticmethod
    def all_projects(cls,data):
        query = "SELECT * from projects"

        results = connectToMySQL(db).query_db(query)
        projects = []
        if results < 1 :
            return False
        for i in results:
            projects.append( cls(i) )
        return projects