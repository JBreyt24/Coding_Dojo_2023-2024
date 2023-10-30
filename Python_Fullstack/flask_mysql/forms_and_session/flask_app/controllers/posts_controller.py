from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user_model, post_model

@app.route('/posts')
def all_posts():
    all_posts = post_model.Post.get_all_join_creator()
    return render_template('all_posts.html', all_posts = all_posts)