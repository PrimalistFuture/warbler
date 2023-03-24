from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length, URL


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    email = StringField(
        'E-mail',
        validators=[DataRequired(), Email()],
    )

    password = PasswordField(
        'Password',
        validators=[Length(min=6)],
    )

    image_url = StringField(
        '(Optional) Image URL',
    )


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    password = PasswordField(
        'Password',
        validators=[Length(min=6)],
    )

class EditProfileForm(FlaskForm):
    """Edit user profile form."""

    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    email = StringField(
        'E-mail',
        validators=[DataRequired(), Email()],
    )
    # TODO: url validator
    image_url = StringField(
        '(Optional) Image URL',
    )

    header_image_url = StringField(
        '(Optional) Header Image URL',
    )

    bio = TextAreaField(
        '(Optional) Bio',
    )

    password = PasswordField(
        'Enter current password',
        validators=[DataRequired(), Length(min=6)],
    )


class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection"""