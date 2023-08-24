from flask_app import app 
from flask_app.controllers import rename_controller #replace rename_controller with your controller file name. Do not include .py


from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True, port=5001)