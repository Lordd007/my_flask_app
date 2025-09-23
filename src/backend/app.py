# src/backend/app.py
from flask import Flask
from api.calculator_api import bp as calc_bp
from .health import bp as health_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(calc_bp)

    @app.get("/")
    def index():
        return (
            "<h1>My Flask App</h1>"
            '<p>Health: <a href="/health">/health</a></p>'
            '<p>Try POST /calc/add with JSON {"a":2,"b":3}</p>'
        )

    return app
