from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user_model import User # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

# Create Users Controller

# @app.route('/users', methods = ["post"])
# def create_user():
#     print(f"POST route: {request.form}")
#     if User.validate_user(request.form):
#         data = {
#             "fname": request.form["first_name"],
#             "lname": request.form["last_name"],
#             "age": request.form["age"],
#             "email": request.form["email"],
#             "pw": request.form["password"]
#         }
#         user_id = User.save(data)
#         return redirect('/')
#     return redirect('/')


# Read Users Controller

@app.route('/all_users')
def all_users():
    all_users = User.get_all()
    # print(all_users)
    return render_template('form.html', allUsers = all_users, logged_in_user = User.get_by_id({'id': session['user_id']}))

@app.route('/users/display/<int:user_id>')
def show_one_user(user_id):
    # print(user_id)
    # thisUser = User.get_by_id({"id": user_id})
    #
    thisJoinUser = User.get_by_id_join_posts({"id": user_id})
    print(thisJoinUser)
    # for post in thisJoinUser.posts:
    #     print(post)
    return render_template("display.html", user = thisJoinUser)


# Update Users Controller

@app.route('/users/update/<int:user_id>', methods = ["post"])
def update_user(user_id):
    print(f"POST route: {request.form}")
    data = {
        "fname": request.form["first_name"],
        "lname": request.form["last_name"],
        "email": request.form["email"],
        "id" : user_id
    }
    User.update_by_id(data)
    return redirect('/')

# Delete Users Controller

@app.route('/users/delete/<int:user_id>')
def delete_one_user(user_id):
    # print(user_id)
    User.delete_by_id({"id": user_id})
    return redirect('/')

# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')                                   The variable must be in the path within angle brackets
# def index(id):                                            It must also be passed into the function as an argument/parameter
#     user_info = user.User.get_user_by_id(id)              The it will be able to be used within the function for that route
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.

# Render template is a function that takes in a template name in the form of a string, then any number of named arguments containing data to pass to that template where it will be integrated via the use of jinja
# Redirect redirects from one route to another, this should always be done following a form submission. Don't render on a form submission.