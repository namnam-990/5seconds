from flask import Blueprint, render_template, url_for, request, flash
from werkzeug.utils import redirect
from flask_login import login_user, logout_user, current_user
from five_sec.models import User
bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:  # 계정 존재 + 비밀번호 일치
            login_user(user)
            return redirect('/')

        else:
            flash('아이디 또는 비밀번호가 틀렸습니다.')



    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect('/login')