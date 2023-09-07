from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from datetime import datetime
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField,TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User



class RegistrationForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired(), Length(min=2, max=20, message="Your First Name should be more than 2 characters and less than 20")])
    last_name = StringField("Last name", validators=[DataRequired(), Length(min=2, max=20, message="Your Last Name should be more than 2 characters and less than 20")])
    phone_number = StringField("Phone number", validators=[DataRequired(), Length(min=2, max=20, message="Your Last Name should be more than 2 characters and less than 20")])
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20, message="Your username should be more than 2 characters and less than 20")])
    email =  EmailField("Email", validators=[DataRequired(), Email(message="Please input a valid email"), Length(min=6, max=40, message="Your email should be more than 6 characters and less than 40")])
    address =  StringField("Address", validators=[DataRequired(), Length(min=10, max=200, message="Your Address should be more than 10 characters and less than 200")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7, max=100, message="Your password should be more than 7 characters and less than 100")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", "Passwords does not match!")])
    submit = SubmitField("Sign-Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            raise ValidationError("This username is taken.")
        
    
    def validate_email(self, email):
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            raise ValidationError("This email is taken.")


class LoginForm(FlaskForm):
    email =  EmailField("Email", validators=[DataRequired(), Email(message="Please input a valid email")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7, max=100,  message="Your password should be more than 7 characters and less than 100")])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

    def validate_email(self, email):
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append("Incorrect email.")
            return False

class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20, message="Your username should be more than 2 characters and less than 20")])
    email =  EmailField("Email", validators=[DataRequired(), Email(message="Please input a valid email"), Length(min=6, max=40, message="Your email should be more than 6 characters and less than 40")])
    picture = FileField('Click to upload image', validators=[FileAllowed(['jpg', 'png', 'svg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if current_user.username != self.username.data:
            user = User.query.filter_by(username=self.username.data).first()
            if user:
                raise ValidationError("This username is taken.")
        
    
    def validate_email(self, email):
        if current_user.email != self.email.data:
            user = User.query.filter_by(email=self.email.data).first()
            if user:
                raise ValidationError("This email is taken.")


class ProductPostForm(FlaskForm):
    name =  StringField("Product name", validators=[DataRequired(), Length(min=2, max=50,  message="Your product name should be more than 2 characters and less than 50")])
    price = StringField("Price", validators=[DataRequired(), Length(min=1, max=20,  message="Your price should be more than 1 characters and less than 20")])
    product_url = StringField("Product URL", validators=[DataRequired(), Length(min=1, max=500,  message="Your product url should be more than 1 characters and less than 20")])
    category = StringField("Category", validators=[DataRequired(), Length(min=1, max=20,  message="Your category should be more than 1 characters and less than 20")])
    Description =  TextAreaField("Description", validators=[DataRequired()])
    submit = SubmitField("Post")


class RequestResetForm(FlaskForm):
    email =  EmailField("Email", validators=[DataRequired(), Email(message="Please input a valid email")])
    submit = SubmitField("Request password reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            raise ValidationError({"Response": f" A reset email has been sent to {self.email.data}"})


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired(), Length(min=7, max=100, message="Your password should be more than 7 characters and less than 100")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", "Passwords does not match!")])
    submit = SubmitField("Reset password")
