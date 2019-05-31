from flask import Flask, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from flask import Blueprint
from peewee import *
from flask_bcrypt import Bcrypt

home = Blueprint('home', __name__, template_folder='templates')

@home.route("/")
def index():
    return render_template('index.html')

@home.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    return render_template('signup.html', error=error)
    
@home.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    return render_template('login.html', error=error)

def valid_login(un, pw):
    pass

@home.route("/forgot_password")
def forgot_password():
    return render_template('password.html')

@home.route("/terms_and_conditions")
def toc():
    return render_template('termsandconditions.html')

@home.route("/about")
def about():
    return render_template('about.html')