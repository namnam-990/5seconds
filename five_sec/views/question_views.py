from flask import Blueprint, render_template, url_for, session
from werkzeug.utils import redirect
from sqlalchemy import func
from five_sec.models import Question
import random

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/')
def question():
    session["question_ids"] = list()
    while len(session["question_ids"]) < 5:
        temp_num = random.randint(1, 20)
        if temp_num not in session["question_ids"]:
            session["question_ids"].append(temp_num)

    return redirect(url_for('question.start'))

@bp.route('/start')
def start():
    if len(session["question_ids"]) > 0:
        temp_list = session["question_ids"]
        temp_id = temp_list.pop(0)
        session["question_ids"] = temp_list
        return redirect(url_for('question.question_detail', question_id=temp_id))
    else:
        return redirect(url_for('question.end'))

@bp.route('/<int:question_id>')
def question_detail(question_id):
    question_ = Question.query.get_or_404(question_id)
    return render_template('question_detail.html', question_=question_)

@bp.route('/end')
def end():
    return redirect(url_for('main.hello'))