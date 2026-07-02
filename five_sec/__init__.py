from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import config
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()




def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config["SECRET_KEY"] = "dev-secret-key"

    login_manager.init_app(app)
    login_manager.login_view = 'login.login'

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # LOGIN
    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(int(user_id))

    # bp
    from .views import main_views, question_views, static_views, login_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(static_views.bp)
    app.register_blueprint(login_views.bp)

    return app