from mainApp import db
from datetime import datetime


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(20), unique=True, nullable=False)
    teamCaptain = db.Column(db.String(20), nullable=False)
    teamMember_1 = db.Column(db.String(20))
    teamMember_2 = db.Column(db.String(20))
    type = db.Column(db.String(8), nullable=False)
    themeM = db.Column(db.String(20), nullable=False)
    themeS = db.Column(db.String(20), nullable=False)
    themeE = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.teamName}', '{self.type}')"
