from abc import ABC, abstractmethod
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import SMALLINT, TEXT
from app import create_app


db = SQLAlchemy()
migrate = Migrate()


class Resolution(db.Model):
    """represents resolution table in database"""

    id = db.Column(db.Integer, primary_key=True)
    resolution = db.Column(db.String(100), nullable=False)
    percentage = db.Column(SMALLINT(), default=0)
    description = db.Column(TEXT())

    def __init__(
        self,
        resolution: str,
        percentage: int = None,
        description: str = None
    ) -> None:
        self.resolution = resolution
        self.percentage = percentage
        self.description = description

    def save(self) -> None:
        """save record into database"""

        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    def remove(self) -> None:
        """remove record from database"""

        try:
            db.session.delete(self)
            db.session.commit()
        except Exceptionn:
            db.session.rollback()
            raise

    def jsonify(self) -> dict:
        """jsonify returning row"""

        return {
            "id": self.id,
            "resolution": self.resolution,
            "percentage": self.percentage,
            "description": self.description
        }
