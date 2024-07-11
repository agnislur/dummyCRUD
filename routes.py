from flask import Blueprint, render_template, redirect, url_for, request, session
from controllers.user import add_user_function, edit_user_function, delete_user_function, register_user_function, login_user_function,loginuser_user_function
import sys 
from models.user import User, User1

main = Blueprint('main', __name__) #routename= main

@main.route('/', methods=['GET'])
def home():
    data = User.get_all()
    return render_template('index.html', data=data)

@main.route('/adduser',methods = ['GET','POST'])
def add_user():
    data = add_user_function()
    #print(data, files=sys.stderr)
    return render_template('adduser.html', data=data)

@main.route('/edituser/<int:id>',methods = ['GET','POST'])
def edit_user(id):
    user = User1.get_by_id(id)
    data = edit_user_function(user)

    return render_template('edituser.html', user=user, data=data)

@main.route('/deleteuser/<int:id>', methods=['POST'])
def delete_user(id):
    user = User1.get_by_id(id)
    print(user,file=sys.stderr)
    delete_user_function(user)
    return redirect(url_for('main.home_page'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email == 'admin@gmail.com' and password == 'admin':
            return redirect(url_for('main.home_page'))
        else:
            return "Invalid credentials", 401
    
    # Jika method GET, tampilkan halaman login
    return render_template('login.html')

@main.route('/loginuser', methods=['GET', 'POST'])
def loginuser():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = loginuser_user_function(email, password)
        if user:
            return redirect(url_for('main.home_user'))
        else:
            return "Invalid credentials", 401
    return render_template('loginuser.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = register_user_function(name, email, password)
        if user:
            return redirect(url_for('main.loginuser'))
        else:
            return "Registration failed", 400
    return render_template('register.html')

@main.route('/home', methods=['GET'])
def home_page():
    data = User1.get_all()
    return render_template('home.html', data=data)

@main.route('/homeuser', methods=['GET'])
def home_user():
    data = User1.get_all()
    return render_template('homeuser.html', data=data)
