from flask import request
from models.user import User, User1
from extensions import db

def add_user_function():
    if request.method == "POST":
        name=request.form['name']
        email=request.form['email']
        password= request.form['password']
        user= User1(
            name=name,
            email=email,
            password=password
        )

        user.save()
        data = {
            'id':user.id,
            'name':user.name,
            'email':user.email,
            'password':user.password
        }
        return data
    
def edit_user_function(data):
    if request.method == "POST":
        data.name =request.form['name']
        data.email=request.form['email']
        data.password = request.form['password']

        db.session.commit()
        return data

def delete_user_function(user):
    db.session.delete(user)
    db.session.commit()

def register_user_function(name, email, password):
    try:
        # Create a new user object
        new_user = User1(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except Exception as e:
        print(e)
        return None


def login_user_function(email, password):
    try:
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:  # Anda mungkin ingin menggunakan hashing password yang aman di sini
            return user
        else:
            return None
    except Exception as e:
        print(e)
        return None


def loginuser_user_function(email, password):
    try:
        user = User1.query.filter_by(email=email).first()
        if user and user.password == password:  # Anda mungkin ingin menggunakan hashing password yang aman di sini
            return user
        else:
            return None
    except Exception as e:
        print(e)
        return None