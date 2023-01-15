from flask import Blueprint,render_template, request , flash, redirect, url_for
from .models import User,Task
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import  login_user, login_required, logout_user, current_user
from .import db

auth=Blueprint('auth',__name__)

@auth.route("/home")
def home():
    return render_template("home.html")


@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                print('Logged in successfully!')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                print('Incorrect password, try again.')
        else:
            print('user does not exist.')

    return render_template("login.html",user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        con_pwd = request.form.get('con_pwd')

        user = User.query.filter_by(username=username).first()
        if user:
            print('user already exists.')
        
        elif pwd!=con_pwd:
            print("password doesnt match")
        else:
            print('sucess')
            new_user= User(username=username,password=generate_password_hash(pwd,method='sha256') )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            print("account created")
            return redirect(url_for('views.home'))
    return render_template("signup.html",user=current_user)

