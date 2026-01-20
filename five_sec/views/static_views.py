from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('static', __name__, url_prefix='/')


@bp.route('/static')
def static():
    return render_template('static.html')

