from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'
app.config['SECRET_KEY'] = '9d070d001c4bd65d3670ed30cdf876ec'
db = SQLAlchemy(app)


from mainApp import routes
