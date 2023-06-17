from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos=dojo.Dojo.get_all())

@app.route('/create/ninjas', methods=['POST'])
def create_ninjas():
    ninja.Ninja.save(request.form)
    return redirect('/dojos')