from pymongo import MongoClient
from github import Github

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = MongoClient()

    return g.db


def init_db(username, password):
    db = get_db()
    if db.github_data.users.find_one({'username':username}) is None:
        user = Github(username, password).get_user(username)
        fs = user.get_followers()
        followers = []
        for f in fs:
            followers.append({'name':f.login, 'parent':user.login})
        db.github_data.users.insert_one({
    		'name':user.login,
    		'children':followers,
    		'size':len(followers)
    	})


@click.command('init-db')
@click.argument('username')
@click.password_option()
@with_appcontext
def init_db_command(username, password):
    """Download github user data and store in local mongodb."""
    init_db(username, password)
    click.echo('Initialized the database.')

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
