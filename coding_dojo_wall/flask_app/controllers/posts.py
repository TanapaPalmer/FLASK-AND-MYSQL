from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.post import Post

@app.route("/posts", methods=["POST"])
def posts():
    posting = request.form
    if not Post.validate_post(posting):
        return redirect("/wall")
    Post.save(request.form)
    
    return redirect("/wall")

@app.route('/posts/destroy/<int:post_id>')
def delete(post_id):
    Post.delete(post_id)
    return redirect('/wall')

