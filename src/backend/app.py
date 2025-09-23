from flask import Flask
from src.api.calculator_api import bp as calc_bp
from .health import bp as health_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(calc_bp)
    return app
