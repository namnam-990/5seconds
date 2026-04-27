from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from flask_login import login_user, logout_user, current_user
from five_sec.models import User
bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        login_user(user)
        return redirect('/')



    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect('/')