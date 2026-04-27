from five_sec import db
from flask_login import UserMixin

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # 질문 본문
    subject = db.Column(db.String(200), nullable=False)

    # 카테고리: energy / social / action / mood
    category = db.Column(db.String(20), nullable=False)

    # 선택지 텍스트
    left_text = db.Column(db.String(100), nullable=False)
    right_text = db.Column(db.String(100), nullable=False)

    # 선택 시 점수 (해당 카테고리 기준)
    left_score = db.Column(db.Integer, nullable=False)
    right_score = db.Column(db.Integer, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
