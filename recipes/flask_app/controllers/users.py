from flask_app.models.user import User
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dash():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        'id': session['user_id']
    }
    return render_template("dash.html", user=User.get_by_id(data))

@app.route("/submit", methods=["POST"])
def submit():
    if not User.is_valid_user(request.form):
        return redirect('/')
    data={
        "first_name":request.form["first_name"].lower(),
        "last_name":request.form["last_name"].lower(),
        "email":request.form["email"].lower(),
        "password":bcrypt.generate_password_hash(request.form["password"])
    }

    id=User.save(data)
    session['user_id'] = id
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.generate_password_hash(request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")