from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo, Email, DataRequired,ValidationError
from market.models import User
class RegForm(FlaskForm):
    def validate_username(self,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('username already exist')
    username = StringField(label="username",validators=[Length(min=2,max=30),DataRequired()])
    password = PasswordField(label="pass")
    cpass = PasswordField(label="confirmepass",validators=[EqualTo('password'),DataRequired()])
    email = StringField(label='email',validators=[Email()])
    submit = SubmitField(label="reg")
class LoginForm(FlaskForm):
    username = StringField(label="username",validators=[DataRequired()])
    password = PasswordField(label="password",validators=[DataRequired()])
    submit = SubmitField(label="login")
