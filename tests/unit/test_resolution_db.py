import pytest
from sqlalchemy.exc import IntegrityError
from app.db import db, Resolution


def test_create_resolution_row(resolution):
    """test create new resolution row"""

    new_resolution = Resolution(**resolution)
    new_resolution.save()
    check = Resolution.query.filter_by(
        resolution=new_resolution.resolution
    ).first()

    assert check is not None


def test_create_resolution_row_fail():
    """test create resolution without providing resolution field"""

    with pytest.raises(IntegrityError):
        new_resolution = Resolution(None)
        new_resolution.save()


def test_fetch_one_resolution_row_by_id():
    """test fetch one existing resolution row"""

    resolution = Resolution.query.get(1)

    assert resolution is not None
    assert isinstance(resolution, Resolution)


def test_fetch_all_resolution_row():
    """test fetch all existing resolution row"""

    resolution = Resolution.query.all()

    assert len(resolution) != 0


def test_delete_resolution_row():
    """test delete existing resolution row from database"""

    Resolution.query.delete()
    check_resolution = Resolution.query.first()

    assert check_resolution is None


def test_delete_resolution_row_fail():
    """test delete unexisting resolution row from database"""

    with pytest.raises(Exception):
        resolution = Resolution.query.first()
        db.session.delete(resolution)
        db.session.commit()
