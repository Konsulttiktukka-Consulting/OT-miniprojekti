from flask import Blueprint, flash, g, redirect, render_template, request, url_for

from application import db
from application.blogposts.models import BlogPost
from application.blogposts.forms import BlogPostForm 
from sqlalchemy import text

bp = Blueprint("blogposts", __name__)

@bp.route("/blogposts/new")
def blog_posts_form():
    form = BlogPostForm()
    return render_template("blogposts/new.html", form=form)

@bp.route("/blogposts/", methods=["POST"])
def blog_posts_create():
    form = BlogPostForm(request.form)
    if form.validate_on_submit():
        new_blog_post = BlogPost(form.title.data, form.url.data, form.author.data,form.description.data)
        db.session.add(new_blog_post)
        db.session().commit()
        return redirect(url_for("books.books_index"))

    return url_for("blog_posts_form")

@bp.route("/blogposts/update/<blog_post_id>/", methods=["GET", "POST"])
def blog_posts_update(blog_post_id):
    blog_post = BlogPost.query.get(blog_post_id)
    form = BlogPostForm(request.form)
    if form.validate_on_submit():
        form.populate_obj(blog_post)
        db.session().commit()
        return render_template("blogposts/blogpost.html", blogpost=blog_post)

    form = BlogPostForm(obj=blog_post)
    return render_template("blogposts/update.html", blogpost=blog_post, form=form)

@bp.route("/blogposts/<blog_post_id>", methods=["GET","POST"])
def blog_posts_show(blog_post_id):
    blog_post = BlogPost.query.get(blog_post_id)
    return render_template("blogposts/blogpost.html", blogpost=blog_post)