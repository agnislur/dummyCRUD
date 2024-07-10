from flask import Blueprint, render_template, redirect, url_for
from controllers.user import add_user_function, edit_user_function, delete_user_function
import sys 
from models.user import User

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
    user = User.get_by_id(id)
    data = edit_user_function(user)

    return render_template('edituser.html', user=user, data=data)

@main.route('/deleteuser/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.get_by_id(id)
    print(user,file=sys.stderr)
    delete_user_function(user)
    return redirect(url_for('main.home'))
