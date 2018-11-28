from pymongo import MongoClient
from github import Github

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = MongoClient()

    return g.db

def init_db():
    db = get_db()
    users = Github().get_users()
    with click.progressbar(users) as bar:
        for u in bar:
            db.github_data.users.insert_one(
				{'name':u.login, 'followerurl':u.followersurl}
			)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Download github user data and store in local mongodb."""
    init_db()
    click.echo('Initialized the database.')

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
