from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from GitHubVisualisation.db import get_db
import pymongo

bp = Blueprint('visualisation', __name__)

@bp.route('/')
def index():
    db = get_db()
    followers = db.users.find_one({'name':g.user}, {'followers':1, '_id':0})
    return render_template('visualisation/index.html', followers=followers)
