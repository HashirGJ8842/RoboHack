from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'
app.config['SECRET_KEY'] = '9d070d001c4bd65d3670ed30cdf876ec'
app.config['RC_SECRET_KEY'] = '6LdWh9EUAAAAAOjRDNTJ60RPk14syhihi7bT9ins'
app.config['RC_SITE_KEY'] = '6LdWh9EUAAAAAAJnLuPg2tsNbyT3UCI3cp5SdbPs'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LdWh9EUAAAAAAJnLuPg2tsNbyT3UCI3cp5SdbPs'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LdWh9EUAAAAAOjRDNTJ60RPk14syhihi7bT9ins'
db = SQLAlchemy(app)


from mainApp import routes
