from flask_wtf import FlaskForm 
from wtforms import (
    StringField ,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)

from wtforms.validators import(
    DataRequired,
    Length,
    Email,
    EqualTo,
    Optional
)

class signupForm(FlaskForm):
    username=StringField(
        "Username",  #here this will show the user as label
        validators=[DataRequired(),Length(3,25)]
    )
    email=StringField(
        "Email" ,
        validators=[DataRequired(),Email()]
    )
    gender=SelectField(
        "Gender" ,
        choices=[
            ("", "Select Gender"), 
            ("male", "Male"), 
            ("female", "Female"), 
            ("other", "Other")
        ],
        validators=[Optional()]
    )
    dob=DateField(
        "Date of Birth" ,
        validators=[Optional()]
    )
    password=PasswordField(
        "Password" ,
        validators=[DataRequired(),Length(5,15)]
    )
    checkPassword=PasswordField(
        "confirm password",
        validators=[DataRequired(),EqualTo("password",message="Passwords must match.")]
    )
    remember_me = BooleanField(
        "Remember Me"
    )

    submit=SubmitField("sign Up")



class LoginForm(FlaskForm):
    email=StringField(
        "Email",  #here this will show the user as label
        validators=[DataRequired(),Email()]
    )
    password=PasswordField(
        "Password" ,
        validators=[DataRequired(),Length(5,15)]
    )
    Submit=SubmitField("Login")
