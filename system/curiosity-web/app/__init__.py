from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.routes.system import system as system_blueprint
    app.register_blueprint(system_blueprint)

    from app.routes.manifest import manifest as manifest_blueprint
    app.register_blueprint(manifest_blueprint)

    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
