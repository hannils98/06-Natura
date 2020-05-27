from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Användarnamn', validators=[DataRequired()])
    password = PasswordField('Lösenord', validators=[DataRequired()])
    remember_me = BooleanField('Kom ihåg mig')
    submit = SubmitField('Logga in')


class RegistrationForm(FlaskForm):
    username = StringField('Användarnamn', validators=[DataRequired()])
    email = StringField('E-post', validators=[DataRequired(), Email()])
    password = PasswordField('Lösenord', validators=[DataRequired(), Length(min=6, message='Välj minst 6 tecken.')])
    password2 = PasswordField(
        'Bekräfta lösenord', validators=[DataRequired(), EqualTo('password', message='Lösenorden måste matcha.')])
    submit = SubmitField('Registrera')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Välj ett annat användarnamn.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Använd en annan e-postadress.')


class EditProfileForm(FlaskForm):
    username = StringField('Användarnamn', validators=[DataRequired()])
    about_me = TextAreaField('Om mig', validators=[Length(min=0, max=140)])
    submit = SubmitField('Uppdatera')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Välj ett annat användarnamn.')


class PostForm(FlaskForm):
    post = TextAreaField('Gör ett nytt inlägg:', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Skicka')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('E-post', validators=[DataRequired(), Email()])
    submit = SubmitField('Begär återställning av lösenord')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Lösenord', validators=[DataRequired()])
    password2 = PasswordField(
        'Bekräfta lösenord', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Begär återställning av lösenord')


class DeleteUserForm(FlaskForm):
    username = StringField('Användarnamn', validators=[DataRequired()])
    password = PasswordField('Lösenord', validators=[DataRequired()])
    delete = SubmitField('Ta Bort')

class ContactForm(FlaskForm):
    name = StringField('Ditt namn', validators=[DataRequired()])
    email = StringField('Din e-post (ifall du vill att vi kontakta dig)')
    subject= StringField('Subjekt')
    message = TextAreaField('Vad vill du säga till oss?', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Skicka')

class SearchForm(FlaskForm):
  search = StringField('Sök efter användare:', [DataRequired()])
  submit = SubmitField('Sök',
                       render_kw={'class': 'btn btn-success btn-block'})