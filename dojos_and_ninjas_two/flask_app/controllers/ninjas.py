from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import dojo, ninja
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos=dojo.Dojo.get_all())

@app.route('/create/ninjas', methods=['POST'])
def create_ninjas():
    ninja.Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/ninjas/edit/<int:id>/<int:dojo_id>')
def edit(id, dojo_id):
    data ={
        'id': id
    }   
    dojo_data = {
        'id': dojo_id
    }    
    return render_template('edit.html', ninja=Ninja.get_one(data), dojos=Dojo.get_all(), dojo=Dojo.get_by_id(dojo_data))

@app.route('/ninjas/update/<int:id>/<int:dojo_id>', methods=['POST'])
def update(id, dojo_id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.update(data)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/ninjas/delete/<int:id>/<int:dojo_id>')
def delete(id, dojo_id):
    data = {
        'id': id
    }
    Ninja.delete(data)
    return redirect(f'/dojos/{dojo_id}')
    