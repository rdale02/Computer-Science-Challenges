from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Reg Form has fields for Username, Email, Password, ConfirmPassword and Submit
class RegForm(FlaskForm):
    username = StringField("Username",validators = [DataRequired(), Length(min = 2, max = 16)])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password",validators =[DataRequired(),Length(min = 8, max = 16)])
    confirm_password = PasswordField("Confirm Password",validators = [DataRequired(),EqualTo("Password")])
    submit = SubmitField("Register")

#Login Form has fields for Email, Password, RememberMe? and Submit Button
class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password",validators =[DataRequired(),Length(min = 8, max = 16)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")