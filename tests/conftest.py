import os
import pytest
import tempfile
from app import create_app
from app.db import db


@pytest.fixture(scope="session")
def app():
    """return flask object for the whole session"""

    # required as temporary db file
    db_fd, db_path = tempfile.mkstemp()
    flask_app = create_app(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{db_path}"
    )

    yield flask_app

    os.close(db_fd)
    os.remove(db_path)


@pytest.fixture(scope="session", autouse=True)
def context(app):
    """create application context for the whole session"""

    with app.app_context():
        # create context once
        # let all the test use it for the whole session
        db.create_all()
        yield


@pytest.fixture()
def client(app):
    """return test client obj to all the individual steps"""

    with app.test_client() as client:
        return client


@pytest.fixture()
def resolution():
    """provide resolution fields for testing"""

    return {
        "resolution": "Learning Linux System Administration",
        "percentage": 50,
        "description": "it's still on-going"
    }
