from flask import render_template, url_for, request, redirect, flash, session
from app import app, db
from app.models import Users, Games
from app.forms import LoginForm, RegisterForm
from flask_bcrypt import generate_password_hash

from app.helpers import is_credentials_valid, user_not_logged, PAGE_NAME


@app.route('/')
def index():
    if (user_not_logged(session)):
        return redirect(url_for('login'))

    return render_template('index.html', games=Games.query.order_by(Games.id))


@app.route('/login')
def login():
    if (user_not_logged(session)):
        return render_template('login.html', title=('Entrar | ' + PAGE_NAME), form=LoginForm())

    return redirect(url_for('index'))


@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'POST':
        form = LoginForm(request.form)
        user = Users.query.filter_by(username=form.username.data).first()

        # << CASE 1: SUCCESS >>
        if (is_credentials_valid(user, user.password, form.password.data)):
            session['user'] = user.username

            flash('Bem-vindo ' + user.username + ".", 'success')

            return redirect(url_for('index'))
        # << CASE 2: ERROR >>
        else:
            flash('Nome de usuário ou senha inválidos.', 'error')

            return redirect(url_for('login'))

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    if (not user_not_logged(session)):
        session['user'] = None

        flash('Usuário deslogado com sucesso!', 'success')

        return redirect(url_for('login'))

    return redirect(url_for('index'))


@app.route('/signup')
def signup():
    if (user_not_logged(session)):
        return render_template('signup.html', title=('Nova Conta | ' + PAGE_NAME), form=RegisterForm())

    return redirect(url_for('index'))


@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        form = RegisterForm(request.form)
        username = form.username.data
        user = Users.query.filter_by(username=username).first()
        redirect_page = 'signup'

        # << CASE 1: ERROR (USER EXISTS) >>
        if (user):
            flash('Já existe um usuário com este nome.', 'error')

            return redirect(url_for(redirect_page))
        # << CASE 2: ERROR (INVALID FORM) >>
        elif (not form.validate()):
            flash('Preencha os dados corretamente.', 'error')

            return redirect(url_for(redirect_page))
        # << CASE 3: SUCCESS >>
        else:
            password = generate_password_hash(
                form.password.data).decode("utf-8")
            new_user = Users(username=username, password=password)

            db.session.add(new_user)
            db.session.commit()

            flash('Usuário cadastrado com sucesso!', 'success')

            return redirect(url_for('login'))

    return redirect(url_for('index'))


# ---------------------------------------------------------------
