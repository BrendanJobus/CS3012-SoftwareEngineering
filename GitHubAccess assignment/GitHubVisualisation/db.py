from pymongo import MongoClient
from github import Github

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = MongoClient()

    return g.db

def generateTree(github, username, level, namesSoFar):
    user = github.get_user(username)
    fs = user.get_followers()
    tree = []
    for f in fs:
        fname = f.login # save on rate limit
        if fname not in namesSoFar:
            namesSoFar.append(fname)
            if level > 1 or f.get_followers().totalCount is 0:
                tree.append({'name':fname, 'parent':user.login})
            else:
                tree.append({'name':fname, 'parent':user.login, 'children':generateTree(github, fname, level+1, namesSoFar)})
    return tree


def init_db(username, password):
    db = get_db()
    username = Github().get_user(username).login	# takes care of any case sensitivities in db
    if db.github_data.trees.find_one({'name':username}) is None:
        authGithub = Github(username, password)
        tree = generateTree(authGithub, username, 0, [username])
        db.github_data.trees.insert_one({
            'name':username,
            'children':tree
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
