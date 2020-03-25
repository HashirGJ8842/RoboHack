from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    teamname = StringField('Team Name', validators=[DataRequired(), Length(min=2, max=20)])
    teamCaptain = StringField('Team Captain', validators=[DataRequired(), Length(min=2, max=20)])
    teamSize = SelectField('Team Size', validators=[DataRequired()], choices=[('0', 'Please select one'), ('1', '1'), ('2', '2'), ('3', '3')])
    teamMember_1 = StringField('Member 1', validators=[Length(min=2, max=20)])
    teamMember_2 = StringField('Member 2', validators=[Length(min=2, max=20)])
    themesS = SelectField('Theme', validators=[DataRequired()], choices=[('None', 'Select'), ('smart', 'Smart City/ Swachh Bharat'), ('sustain', 'Sustainable Development'), ('health', 'HealthCare and Biomedical Services'), ('security', "Security and Surveillance"), ('innovate', 'Student Innovation'), ('COVID', 'COVID-19 and Quarantine')])
    themesE = SelectField('Theme', validators=[DataRequired()],
                          choices=[('None', 'Select'), ('smart', 'Smart City/ Swachh Bharat'),
                                   ('sustain', 'Sustainable Development'),
                                   ('health', 'HealthCare and Biomedical Services'),
                                   ('security', "Security and Surveillance"), ('innovate', 'Student Innovation'),
                                   ('COVID', 'COVID-19 and Quarantine')])
    themesM = SelectField('Theme', validators=[DataRequired()],
                          choices=[('None', 'Select'), ('arm', 'Robotic Arm'),
                                   ('solar', 'Origami Based Solar Panels'),
                                   ('wheel', 'Advanced Wheel Steering Mechanism'),
                                   ('e_vehicle', "Driverless E-Vehicle Design"), ('mask', 'COVID-19 Mask')])
    type = SelectField('Type', validators=[DataRequired()],
                         choices=[('None', 'Select'), ('software', 'Software'),
                                  ('electronics', 'Electronics'),
                                  ('mechanical', 'Mechanical Design')])
    submit = SubmitField('Signup')
    recaptcha = RecaptchaField()