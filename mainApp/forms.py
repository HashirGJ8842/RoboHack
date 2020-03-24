from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    teamname = StringField('Team Name', validators=[DataRequired(), Length(min=2, max=20)])
    teamCaptain = StringField('Team Captain', validators=[DataRequired(), Length(min=2, max=20)])
    teamMember_1 = StringField('Member 1', validators=[Length(min=2, max=20)])
    teamMember_2 = StringField('Member 2', validators=[Length(min=2, max=20)])
    themes = SelectField('Theme', validators=[DataRequired()], choices=[('None', 'Select'), ('smart', 'Smart City/ Swachh Bharat'), ('sustain', 'Sustainable Development'), ('health', 'HealthCare and Biomedical Services'), ('security', "Security and Surveillance"), ('innovate', 'Student Innovation'), ('COVID', 'COVID-19 and Quarantine')])
    submit = SubmitField('Signup')
    recaptcha = RecaptchaField()
    member = BooleanField('Roboclub Member in your team?', validators=[DataRequired()])