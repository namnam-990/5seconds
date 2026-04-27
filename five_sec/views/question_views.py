from flask import Blueprint, render_template, url_for, session
from werkzeug.utils import redirect
from sqlalchemy import func
from flask_login import login_required
from five_sec.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/')
@login_required
def question():
    questions = Question.query.order_by(func.random()).limit(5).all()
    session["question_ids"] = [q.id for q in questions]
    return redirect(url_for('question.start'))

@bp.route('/start')
@login_required
def start():
    if len(session["question_ids"]) > 0:
        temp_list = session["question_ids"]
        temp_id = temp_list.pop(0)
        session["question_ids"] = temp_list
        return redirect(url_for('question.question_detail', question_id=temp_id))
    else:
        return redirect(url_for('question.end'))

@bp.route('/<int:question_id>')
@login_required
def question_detail(question_id):
    question_ = Question.query.get_or_404(question_id)
    return render_template('question_detail.html', question_=question_)

@bp.route('/end')
@login_required
def end():
    return redirect(url_for('main.hello'))