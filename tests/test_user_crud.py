from app.db_control.crud_user import create_user
from app.db_control.models import User


def test_create_user(db):
    """
    Test that a new user is successfully created.
    """
    user = create_user(name="Test User", email="test@example.com", age=25)

    assert user.name == "Test User"
    assert user.email == "test@example.com"
    assert user.age == 25

    # Verify the user exists in the database
    db_user = db.query(User).filter_by(email="test@example.com").first()
    assert db_user is not None
    assert db_user.name == "Test User"
    assert db_user.age == 25
