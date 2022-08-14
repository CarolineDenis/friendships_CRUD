from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import friendship_model
from flask_app.models import user_model

@app.route('/')
def index():
    friends = friendship_model.Friendship.get_all_friendships()
    users = user_model.User.get_all()
    return render_template("index.html", friends=friends, users=users)

@app.route('/add_user', methods=["POST"])
def add_user():    
    data= {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    user_model.User.save(data)
    return redirect('/')