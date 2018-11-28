import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from github import Github, BadCredentialsException
from GitHubVisualisation.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        usr = request.form['username']
        pwd = request.form['password']

        github = Github(usr, pwd)
        try:
            id = github.get_user().login

            session.clear()
            session['user_id'] = id
            return redirect(url_for('index'))

        except BadCredentialsException:
            flash("Invalid username or password.")

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = Github().get_user(user_id)
