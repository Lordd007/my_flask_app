# src/backend/app.py
from flask import Flask, request
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
            "<h2>Enter a Word</h2>"
            '<form method="POST" action="/submit">'
            '<input type="text" name="user_input" placeholder="Type something"/>'
            '<button type="submit">Submit</button>'
            "</form>"
        )

    @app.post("/submit")
    def submit():
        user_text = request.form.get("user_input", "")
        return f"<h1>You entered: {user_text}</h1><br><a href='/'>Go Back</a>"

    return app
