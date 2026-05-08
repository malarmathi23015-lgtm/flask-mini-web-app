from flask import Flask

from app.extensions import (
    db,
    login_manager,
    csrf,
    migrate
)

from app.auth import auth

from app.models.user import User
from app.models.note import Note


def create_app():

    app = Flask(__name__)

    # CONFIG
    app.config['SECRET_KEY'] = 'super-secret-key'

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'sqlite:///app.db'
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # INITIALIZE EXTENSIONS
    db.init_app(app)

    login_manager.init_app(app)

    csrf.init_app(app)

    migrate.init_app(app, db)

    # LOGIN SETTINGS
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(int(user_id))

    # REGISTER BLUEPRINT
    app.register_blueprint(auth)

    return app