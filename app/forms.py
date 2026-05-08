from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    TextAreaField
)

from wtforms.validators import (
    DataRequired,
    Email,
    Length
)


# REGISTER FORM
class RegisterForm(FlaskForm):

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    submit = SubmitField('Register')


# LOGIN FORM
class LoginForm(FlaskForm):

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Login')


# NOTE FORM
class NoteForm(FlaskForm):

    title = StringField(
        'Title',
        validators=[
            DataRequired()
        ]
    )

    content = TextAreaField(
        'Content',
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField('Save Note')