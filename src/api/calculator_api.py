from flask import Blueprint, jsonify, request
from src.backend.components.calculator.calculator import Calculator

bp = Blueprint("calculator", __name__, url_prefix="/calc")
_calc = Calculator()

@bp.post("/add")
def add():
    data = request.get_json(silent=True) or {}
    return jsonify(result=_calc.add(data.get("a", 0), data.get("b", 0)))

@bp.post("/subtract")
def subtract():
    data = request.get_json(silent=True) or {}
    return jsonify(result=_calc.subtract(data.get("a", 0), data.get("b", 0)))
