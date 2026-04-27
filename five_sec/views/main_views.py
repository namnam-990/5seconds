from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from flask_login import login_required

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
@login_required
def hello():
    return render_template('hello.html')

