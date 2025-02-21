from flask import Flask
from .config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Eklentileri başlat
    db.init_app(app)
    migrate.init_app(app, db)

    # Modelleri import et (Flask-Migrate için gerekli)
    from .models import user, text_content

    # Blueprint'leri kaydet
    from .routes.text_routes import text_bp
    from .routes.user_routes import user_bp
    app.register_blueprint(text_bp)
    app.register_blueprint(user_bp)

    return app