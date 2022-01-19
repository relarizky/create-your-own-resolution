from flask import Flask


def create_app(**config: dict) -> Flask:
    """object factory"""

    app = Flask(
        __name__,
        static_folder="static/asset/",
        template_folder="static/template"
    )
    app.config.from_pyfile("config.py")

    if len(config) != 0:
        app.config.update(config)

    from app.db import db, migrate
    from app.api import api, ResolutionAPI, ResolutionAPIWithId

    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)

    from app.controller import home_bp

    api.add_resource(ResolutionAPI, "/resolution/")
    api.add_resource(ResolutionAPIWithId, "/resolution/<int:id>")
    app.register_blueprint(home_bp, url_prefix="/")

    return app
