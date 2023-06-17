from flask_app import app

from flask import session, redirect, render_template, request, flash

from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route("/users")
def users():
    return render_template("users.html", users=User.get_all())

@app.route('/users/add', methods=['POST'])
def add_users():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/users/create')
def new_users():
    return render_template("new.html")

@app.route('/users/<int:id>')
def show(id):
    data = {
        'id':id
    }
    return render_template("show.html", users=User.get_one(data))


@app.route('/users/<int:id>/edit')
def edit(id):
    data ={
        'id': id
    }
    return render_template("edit.html", users=User.get_one(data))

@app.route('/users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/<int:id>/destroy')
def delete(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)
