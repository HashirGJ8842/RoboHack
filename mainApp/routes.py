from mainApp.models import Team
from flask import render_template, redirect, flash, url_for
from mainApp.forms import RegistrationForm
from mainApp import app, db
db.create_all()


@app.route("/", methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    print("Hi")
    if form.validate_on_submit():
        print("Helelelo")
        print(f'{form.teamCaptain.data}')
        print(f'{form.teamname.data}')
        new = Team(teamName=f'{form.teamname.data}', teamCaptain=form.teamCaptain.data,
                     teamMember_1=form.teamMember_1.data, teamMember_2=form.teamMember_2.data,
                     type=form.type.data, themeM=form.themesM.data, themeS=form.themesS.data, themeE=form.themesE.data)
        db.session.add(new)
        db.session.commit()
        print("LOOOOOOOO")
        flash(f'Entry for Team {form.teamname.data} is successful')
    return render_template("laout.html", form=form)

