from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config["SECRET_KEY"] = "dev-secret-key"

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # bp
    from .views import main_views, question_views, static_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(static_views.bp)

    return app