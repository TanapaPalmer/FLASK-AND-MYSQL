from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos = dojos)
    
@app.route('/create/dojos', methods=['POST'])
def create_dojos():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    return render_template('dojos_location.html', dojo=Dojo.get_one_ninja(data))
