# routes are different url's that the application implements.
# In flask, handlers for application routes are written as python functions, called view functions
# view functions are mapped to one or more route URL's so that flask knows what logic to execute 
# when a client requests a specific URL

from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

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
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, \
        remember_me = {form.remember_me.data}")
        return redirect("/index")
    return render_template("login.html", title="Sign in", form=form)
