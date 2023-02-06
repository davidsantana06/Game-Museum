from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, validators
from wtforms_validators import Alpha, AlphaNumeric


class GameForm(FlaskForm):
    name = StringField('Nome do Jogo', validators=[
        validators.DataRequired(),
        validators.length(min=5, max=50),
        AlphaNumeric()
    ])

    plataform = StringField('Plataforma', validators=[
        validators.DataRequired(),
        validators.length(min=2, max=30),
        AlphaNumeric()
    ])
    
    '''
    mushrooms = IntegerField('Cogumelos', validators=[
        validators.DataRequired(),
        validators.length(min=1, max=5)
    ])
    '''

    submit = SubmitField('Salvar')


class LoginForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[
        validators.DataRequired(),
        validators.length(min=4, max=12),
        AlphaNumeric()
    ])

    password = PasswordField('Senha', validators=[
        validators.DataRequired(),
        
    ])

    submit = SubmitField('Entrar')


class RegisterForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[
        validators.DataRequired(),
        validators.length(min=4, max=12),
        AlphaNumeric()
    ])

    password = PasswordField('Senha', validators=[
        validators.DataRequired(),
        validators.length(min=4, max=100),
        AlphaNumeric(),
    ])

    password_confirm = PasswordField('Confirmar', validators=[
        validators.DataRequired(),
        validators.EqualTo('password')
    ])

    submit = SubmitField('Cadastrar-se')
