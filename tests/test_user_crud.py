from app.db_control.crud_user import create_user, get_user_by_id, update_user, delete_user
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


def test_get_user_by_id(db):
    """
    Test retrieving a user by ID.
    """
    # Create a test user
    user = create_user(name="Test User", email="testuser@example.com", age=30)

    # Retrieve the user by ID
    retrieved_user = get_user_by_id(user.id)

    # Verify the retrieved user matches the created user
    assert retrieved_user is not None
    assert retrieved_user.id == user.id
    assert retrieved_user.name == "Test User"
    assert retrieved_user.email == "testuser@example.com"
    assert retrieved_user.age == 30

    # Test non-existent ID returns None
    non_existent_user = get_user_by_id(9999)
    assert non_existent_user is None


def test_update_user(db):
    """
    Test updating a user's details.
    """
    # Create a test user
    user = create_user(name="Old Name", email="oldemail@example.com", age=40)

    # Update the user's details
    updated_user = update_user(user.id, name="New Name", email="newemail@example.com", age=45)

    # Verify the user is updated correctly
    assert updated_user is not None
    assert updated_user.id == user.id
    assert updated_user.name == "New Name"
    assert updated_user.email == "newemail@example.com"
    assert updated_user.age == 45

    # Retrieve user from the database to confirm changes
    db_user = get_user_by_id(user.id)
    assert db_user is not None
    assert db_user.name == "New Name"
    assert db_user.email == "newemail@example.com"
    assert db_user.age == 45

    # Test updating non-existent user returns None
    non_existent_update = update_user(9999, name="Non Existent")
    assert non_existent_update is None


def test_delete_user(db):
    """
    Test deleting a user by ID.
    """
    # Create a test user
    user = create_user(name="Delete Test", email="deletetest@example.com", age=30)

    # Delete the user
    delete_result = delete_user(user.id)

    # Verify deletion succeeded
    assert delete_result is True

    # Confirm user no longer exists in the database
    db_user = get_user_by_id(user.id)
    assert db_user is None

    # Test deleting a non-existent user returns False
    delete_non_existent = delete_user(9999)
    assert delete_non_existent is False

