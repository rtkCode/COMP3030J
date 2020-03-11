from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, RadioField, FileField, DateTimeField,TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed
class LoginForm(FlaskForm):  #line 5-9,11-17 is code from lecture 15 form.py LoginForm and SignUpForm
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class SignUpForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired()])
    accept_rules = BooleanField('I accept the site rules',validators=[DataRequired()])
    submit = SubmitField('Register')

class ProfileForm(FlaskForm):#line 19-23 is inspired from lecture 15 form.py ProfileForm, I change some the field
    dob = DateField('Date of Birth',validators=[DataRequired()])
    phone = StringField('Phone',validators=[DataRequired()])
    gender = RadioField('Gender',choices = [('0','Male'),('1','Female')], validators=[DataRequired()])
    submit = SubmitField('Update Profile')

class PostForm(FlaskForm):#line 25-28 is inspired from lecture 15 form.py PostForm, I change some the field
    title = StringField('Post Title',validators=[DataRequired()])
    body = TextAreaField('Post Body',validators=[DataRequired()])
    submit = SubmitField('Upload Post')    

class ReplyForm(FlaskForm):#line 30-32 is inspired from lecture 15 form.py PostForm, I use it as a new form of reply
    body = TextAreaField('Comment Body',validators=[DataRequired()])
    submit = SubmitField('Upload Comment') 