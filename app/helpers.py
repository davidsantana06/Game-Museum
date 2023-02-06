from flask import session
from flask_bcrypt import check_password_hash


PAGE_NAME = 'Game Museum'

def is_credentials_valid(user, input_pwd, user_pwd):
    return (user != None and check_password_hash(input_pwd, user_pwd))


def user_not_logged(session: session):
    return ('user' not in session or session['user'] == None)
