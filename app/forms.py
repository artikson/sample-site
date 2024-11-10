from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField, SelectField, StringField, PasswordField, SubmitField, ValidationError
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo

from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(), Length(min=10, max=100)])
    login = StringField('Логин', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    avatar = FileField('Загрузите свое фото', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Зарегистрироваться')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Данное имя пользователя недоступно. Выберите другое')
        
class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class StudentForm(FlaskForm):
    student = SelectField('student', choices=[], render_kw={'class':'form-control'})

class TeacherForm(FlaskForm):
    teacher = SelectField('teacher', choices=[], render_kw={'class':'form-control'})