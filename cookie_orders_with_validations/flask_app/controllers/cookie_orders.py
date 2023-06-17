from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.cookie_order import Cookie_order

@app.route("/")
@app.route("/cookies")
def index():
    orders = Cookie_order.get_all()
    return render_template("cookies.html", orders=orders)

@app.route("/cookies/new")
def new_order():
    
    return render_template("new_order.html")

@app.route("/cookies/edit/<int:cookie_id>")
def edit_order(cookie_id):
    order = Cookie_order.get_by_id(cookie_id)

    return render_template("edit_order.html", order = order)

@app.route("/cookies", methods=["POST"])
def create_cookie():
    cookie_order = request.form

    if not Cookie_order.is_valid(cookie_order):
        return redirect("/cookies/new")

    Cookie_order.create(cookie_order)
    
    return redirect("/")

@app.route("/cookies/edit/<int:cookie_id>", methods=["POST"])
def update_cookie(cookie_id):
    cookie_order = request.form

    if not Cookie_order.is_valid(cookie_order):
        return redirect(f"/cookies/edit/{cookie_id}")

    Cookie_order.update(cookie_order)
    
    return redirect("/")