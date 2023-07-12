from flask import Flask
from os import path

from .extensions import db
from .extensions import login_manager
from .extensions import mail

DB_NAME = "commerce.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "46face59834549cb75e923414dba7c360890b58ee4c0985caba12b9222d44064"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    # mail config
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = "tchelberwrites@gmail.com"
    app.config['MAIL_PASSWORD'] = "qkecvakviafyhivw"
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    # initializing app features
    db.init_app(app=app)
    login_manager.init_app(app)
    mail.init_app(app)

    from .views import views
    from .auth import auth

    # registering blueprints
    app.register_blueprint(auth)
    app.register_blueprint(views)
    
    from .models import User, BlogPost, Releases
    
    with app.app_context():
        create_database()

    return app


def create_database():
    if not path.exists("e-commerce/" + DB_NAME):
        db.create_all()
        return 0