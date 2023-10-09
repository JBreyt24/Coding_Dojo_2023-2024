from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user_model # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('form.html')


# Create Users Controller


@app.route('/register', methods = ["post"])
def register():
    # validate user form info
    print(f"POST route: {request.form}")
    if user_model.User.validate_user(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            # "age": request.form["age"],
            "email": request.form["email"],
            "password": pw_hash
        }
        user_id = user_model.User.save(data)
        # print(user_id)
        session['user_id'] = user_id
        session['first_name'] = request.form['first_name']
        return redirect('/welcome')
    # if validation False redirect to form.html
    return redirect('/')



# Read Users Controller


@app.route('/welcome')
def welcome():
    data = {
        "id": session['user_id']
    }
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('welcome.html', user = user_model.User.get_by_id(data))


@app.route('/login', methods = ['post'])
def login():
    data = { 
        "email" : request.form['email'] 
        }
    user_in_db = user_model.User.get_by_email(data)
    if user_in_db:
        if bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            session['user_id'] = user_in_db.id
            return redirect('/welcome')
    flash("Invalid Email/Password")
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# Update Users Controller



# Delete Users Controller




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