from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from five_sec.models import Question

bp = Blueprint('question', __name__, url_prefix='/')


@bp.route('/question')
def question():
    return render_template('question.html')
@bp.route('/question/list')
def question_list():
    question_list = Question.query.all()
    return render_template('question_list.html', question_list=question_list)

