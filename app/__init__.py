from flask import Flask
# pyrefly: ignore [missing-import]
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
# pyrefly: ignore [missing-import]
from flask_login import LoginManager
from config import Config

# Initialize extensions here (do not bind them to the app yet)
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(render_as_batch=True)
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Configure login manager
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Lütfen bu sayfayı görüntülemek için giriş yapın.'

    # Register blueprints
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Import models so Flask-Migrate can detect them
    from app import models

    return app
