from mainApp.models import User
from flask import render_template, redirect, flash, url_for
from mainApp.forms import RegistrationForm
from mainApp import app


@app.route("/", methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template("Register.html", title="Register", form = form)