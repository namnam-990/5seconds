# 5seconds

> 5초 안에 선택하는 성격 유형 테스트

## 소개

**5seconds**는 빠른 직관으로 답하는 성격 유형 퀴즈 앱입니다.
생각할 시간 없이 5초 안에 선택하면서 나의 에너지, 사교성, 행동 방식, 감정 패턴을 알아볼 수 있습니다.

## 기술 스택

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Migrate
- **Database:** SQLite
- **Frontend:** HTML, Bootstrap 5.3

## 프로젝트 구조

```
5seconds/
├── config.py
├── five_sec/
│   ├── __init__.py            # 앱 팩토리
│   ├── models.py              # Question 모델
│   ├── views/
│   │   ├── main_views.py      # 홈 라우트
│   │   ├── question_views.py  # 퀴즈 로직
│   │   └── static_views.py
│   └── templates/
│       ├── hello.html
│       ├── question_detail.html
│       └── static.html
└── migrations/
```

## 실행 방법

```bash
pip install flask flask-sqlalchemy flask-migrate
flask db upgrade
flask run
```

`http://localhost:5000` 접속

## 퀴즈 방식

1. 홈 화면에서 시작
2. 20개 질문 중 랜덤 5개 출제
3. 각 질문마다 두 선택지 중 하나 선택 (5초 이내)
4. energy / social / action / mood 점수 집계
5. 결과 확인

## 점수 카테고리

| 카테고리 | 설명 |
|----------|------|
| energy | 에너지 방향 (내향 ↔ 외향) |
| social | 사교성 (개인 ↔ 집단) |
| action | 행동 방식 (즉흥 ↔ 계획) |
| mood | 감정 패턴 (이성 ↔ 감성) |