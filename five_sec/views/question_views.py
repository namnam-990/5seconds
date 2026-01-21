from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from sqlalchemy import func
from five_sec.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/')
def question():
    return render_template('question.html')
@bp.route('/list')
def question_list():
    question_list = (
        Question.query
        .order_by(func.random())
        .limit(5)
        .all()
    )
    return render_template('question_list.html', question_list=question_list)

@bp.route('/<int:question_id>')
def question_detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question_detail.html', question=question)