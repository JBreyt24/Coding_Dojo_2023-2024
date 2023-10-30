from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user_model, post_model # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# Create Users Controller

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/register', methods = ["post"])
def create_user():
    # validate user form info
    print(f"POST route: {request.form}")
    if user_model.User.validate_user(request.form):
        #
        #
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            "fname": request.form["first_name"],
            "lname": request.form["last_name"],
            "age": request.form["age"],
            "email": request.form["email"],
            "pw": pw_hash
        }
        user_id = user_model.User.save(data)
        # print(user_id)
        session['user_id'] = user_id
        return redirect('/all_users')
    # if validation False redirect to form.html
    return redirect('/')

#create a login function/route
@app.route('/login', methods = ['post'])
def login():
    #
    data = { "email" : request.form['email'] }
    user_in_db = user_model.User.get_by_email(data)
    #
    if user_in_db:
        if bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    #
            session['user_id'] = user_in_db.id
    #
            return redirect('/all_users')
    flash("Invalid Email/Password")
    return redirect('/')


#create a logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')