from flask import Blueprint, render_template, url_for, session
from werkzeug.utils import redirect
from sqlalchemy import func
from flask_login import login_required, current_user
from five_sec import db
from five_sec.models import Question, Static

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/')
@login_required
def question():
    questions = Question.query.order_by(func.random()).limit(5).all()
    session["question_ids"] = [q.id for q in questions]

    stat = Static.query.get(current_user.id)
    session["scores_before"] = {
        'energy': stat.energy if stat else 0,
        'social': stat.social if stat else 0,
        'action': stat.action if stat else 0,
        'mood':   stat.mood   if stat else 0,
    }

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

@bp.route('/<int:question_id>/choose/<side>')
@login_required
def choose(question_id, side):
    question_ = Question.query.get_or_404(question_id)
    score = question_.left_score if side == 'left' else question_.right_score

    stat = Static.query.get(current_user.id)
    if stat is None:
        stat = Static(id=current_user.id, energy=0, social=0, action=0, mood=0)
        db.session.add(stat)

    setattr(stat, question_.category, getattr(stat, question_.category) + score)
    db.session.commit()

    return redirect(url_for('question.start'))

@bp.route('/end')
@login_required
def end():
    stat  = Static.query.get(current_user.id)
    before = session.get("scores_before", {'energy': 0, 'social': 0, 'action': 0, 'mood': 0})

    after = {
        'energy': stat.energy if stat else 0,
        'social': stat.social if stat else 0,
        'action': stat.action if stat else 0,
        'mood':   stat.mood   if stat else 0,
    }

    max_score = 80

    categories = [
        {'key': 'energy', 'label': '에너지', 'icon': '⚡',
         'before_pct': round(before['energy'] / max_score * 100),
         'after_pct':  round(after['energy']  / max_score * 100),
         'delta': after['energy'] - before['energy']},
        {'key': 'social', 'label': '사회성', 'icon': '🤝',
         'before_pct': round(before['social'] / max_score * 100),
         'after_pct':  round(after['social']  / max_score * 100),
         'delta': after['social'] - before['social']},
        {'key': 'action', 'label': '행동력', 'icon': '🎯',
         'before_pct': round(before['action'] / max_score * 100),
         'after_pct':  round(after['action']  / max_score * 100),
         'delta': after['action'] - before['action']},
        {'key': 'mood',   'label': '기분',   'icon': '😊',
         'before_pct': round(before['mood']   / max_score * 100),
         'after_pct':  round(after['mood']    / max_score * 100),
         'delta': after['mood'] - before['mood']},
    ]

    return render_template('result.html', categories=categories)