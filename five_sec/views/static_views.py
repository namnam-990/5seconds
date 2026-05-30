from flask import Blueprint, render_template
from flask_login import login_required, current_user
from five_sec.models import Static

bp = Blueprint('static', __name__, url_prefix='/')


@bp.route('/static')
@login_required
def static():
    stat = Static.query.get(current_user.id)
    if stat is None:
        stat = Static(id=current_user.id, energy=0, social=0, action=0, mood=0)

    scores = {
        'energy': stat.energy,
        'social': stat.social,
        'action': stat.action,
        'mood':   stat.mood,
    }
    max_score = 80

    categories = [
        {'key': 'energy', 'label': '에너지',  'icon': '⚡', 'score': stat.energy, 'pct': max(0, round(stat.energy / max_score * 100))},
        {'key': 'social', 'label': '사회성',  'icon': '🤝', 'score': stat.social, 'pct': max(0, round(stat.social / max_score * 100))},
        {'key': 'action', 'label': '행동력',  'icon': '🎯', 'score': stat.action, 'pct': max(0, round(stat.action / max_score * 100))},
        {'key': 'mood',   'label': '기분',    'icon': '😊', 'score': stat.mood,   'pct': max(0, round(stat.mood   / max_score * 100))},
    ]

    total = sum(scores.values())

    return render_template('static.html', categories=categories, total=total)