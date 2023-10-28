from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User 
from flask_app.models.recipe_model import Recipe 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Create Recipe

@app.route('/recipes/new')
def recipe_create():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('create_recipe.html')

@app.route('/create/recipe', methods = ['POST'])
def create_recipe():
    if not Recipe.validate_recipe_at_create(request.form):
        return redirect('/recipes/new')
    if "user_id" in session:
        recipe_dict = {
            "user_id": session["user_id"],
            "name": request.form['name'],
            "description": request.form['description'],
            "instructions": request.form['instructions'],
            "date": request.form['date'],
            "under_30": request.form['under_30'],
    }
    Recipe.save(recipe_dict)
    return redirect('/welcome')

# Read Recipe

@app.route("/view/recipe/<int:recipe_id>/<int:user_id>")
def view_recipe(recipe_id, user_id):
    if 'user_id' not in session:
        return redirect('/logout')
    recipe = Recipe.get_one(recipe_id)
    user = User.get_one(user_id)
    return render_template("show_recipe.html", recipe = recipe, user = user )

# Update Recipe

@app.route('/edit/recipe/<int:recipe_id>')
def edit_recipe_page(recipe_id):
    if 'user_id' not in session:
        return redirect('/logout')
    recipe = Recipe.get_one(recipe_id)
    return render_template("edit_recipe.html", recipe = recipe)

@app.route("/edit/recipe/<int:recipe_id>", methods = ["POST"])
def edit_recipe(recipe_id):
    if not Recipe.validate_recipe_at_edit(request.form):
        return redirect(f"/edit/recipe/{recipe_id}")
    Recipe.edit_recipe(request.form)
    return redirect('/welcome')

# Delete Recipe

@app.route('/recipe/destroy/<int:recipe_id>')
def destroy_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/logout')
    Recipe.destroy_recipe(recipe_id)
    return redirect('/welcome')