from flask_app.models.user import User
from flask_app import app
from flask import render_template,redirect,request,session,flash

@app.route("/")
def index():
    friends = User.get_all()
    print(friends)
    return render_template("created_page.html", all_friends=friends)

@app.route("/users/create", methods=['POST'])
def create():
    if User.is_valid_user(request.form):
        User.save(request.form)
        return redirect("/")
    else:
        return redirect("/")
