from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User #importing the class here
#There will be other imports need depending what you're trying to use in this file
#You will also need a bycrypt import (we will introduce this week 5)


@app.route('/') #Get request for 127.0.0.1:5000
def home():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods=["POST"])
def create():
    print(request.form)
    User.save(request.form)
    return redirect("/users")

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template("show_user.html", user=User.get_one(data))

@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete', methods=["POST"])
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/users')

# @app.route('/create', methods=['POST'])
# def create():
#     if User.is_valid_user(request.form):
#         User.save(request.form)
#         return redirect('/')
#     else:
#         return redirect('/users/new')