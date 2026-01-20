from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('question', __name__, url_prefix='/')


@bp.route('/question')
def question():
    return render_template('question.html')

