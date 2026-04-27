from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('login', __name__, url_prefix='/')


@bp.route('/')
def static():
    return render_template('static.html')