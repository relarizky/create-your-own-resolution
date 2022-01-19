from flask import Blueprint, render_template
from app import create_app


home_bp = Blueprint("home", __name__)


@home_bp.route("/")
@home_bp.route("/home")
def home():
    """represents home page"""

    return render_template("index.html")


@home_bp.route("/statistic")
def statistic():
    """represents statistic page"""

    return render_template("statistic.html")
