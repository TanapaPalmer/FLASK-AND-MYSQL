from flask import Flask, render_template, redirect, request

from users import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/read')

@app.route("/read")
def users():
    return render_template("users.html", users=User.get_all())

@app.route('/read/add', methods=['POST'])
def add_users():
    print(request.form)
    User.save(request.form)
    return redirect('/read')


@app.route('/read/create')
def new_users():
    return render_template("new.html")



if __name__ == "__main__":
    app.run(debug=True)
