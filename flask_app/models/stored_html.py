from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt



db ='project_manager_db'

class Elements:
    def __init__(self):
        self.navbar = True

    @staticmethod
    def navbars():

        navbar="""<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <div class="container px-5">
                        <a class="navbar-brand" href="/"> <img class="navbar-icon" style="width:50px" src="../../static/img/images/img-01.png"  alt="IMG"> Project Manager</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                        <div class="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                                <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
                                <li class="nav-item"><a class="nav-link" href="/about">About</a></li>
                                <li class="nav-item"><a class="nav-link" href="/contact">Contact</a></li>
                                <li class="nav-item"><a class="nav-link" href="/display/all_projects">Projects</a></li>
                                <li class="nav-item dropdown">
                                    <a class="nav-link dropdown-toggle" id="navbarDropdownPortfolio" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><i class="bi bi-gear"></i></a>
                                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownPortfolio">
                                        <li><a class="dropdown-item" href="/register">Register</a></li>
                                        <li><a class="dropdown-item" href="/login">Login</a></li>
                                        <li><a class="dropdown-item text-danger" href="/logout">Logout</a></li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>"""
        return navbar