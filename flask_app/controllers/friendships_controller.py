from crypt import methods
from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import friendship_model
from flask_app.models import user_model


@app.route('/add_friendship', methods=["POST"])
def add_friendship():
    data={
        'user_id': request.form['user_id'],
        'friend_id': request.form['friend_id']
    }
    friendship_model.Friendship.save(data)    
    return redirect('/')