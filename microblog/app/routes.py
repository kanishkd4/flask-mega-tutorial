# routes are different url's that the application implements.
# In flask, handlers for application routes are written as python functions, called view functions
# view functions are mapped to one or more route URL's so that flask knows what logic to execute 
# when a client requests a specific URL

from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "miguel"}
    posts = [{
        "author": {"username": "John"},
        "body": "Beautiful day in portland"
        },
        {
            "author": {"username": "Susan"},
            "body": "The avengers was so cool"
        }]
    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign in", form=form)
