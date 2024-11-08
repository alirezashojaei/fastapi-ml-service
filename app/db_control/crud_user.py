from typing import Optional

from app.db_control.session import session_scope
from app.db_control.models import User


def create_user(name: str, email: str, age: int = None):
    """
    Creates a new user in the database.

    Args:
    name (str): The name of the user.
    email (str): Email of the user.
    age (int): Age of the user.

    Returns:
    User: The created User object.

    Raises:
    Exception: If the user could not be created due to a database error or constraint violation.
    """

    new_user = User(
        name=name,
        email=email,
        age=age
    )

    with session_scope() as session:
        session.add(new_user)
        try:
            session.flush()
            session.refresh(new_user)
        except Exception as e:
            raise e

    return new_user


def get_user_by_id(user_id: int) -> Optional[User]:
    """
    Retrieves a user by ID.

    Args:
    user_id (int): The ID of the user.

    Returns:
    Optional[User]: The User object if found, otherwise None.
    """
    with session_scope() as session:
        return session.query(User).filter(User.id == user_id).first()


def update_user(user_id: int, name: Optional[str] = None, email: Optional[str] = None,
                age: Optional[int] = None) -> Optional[User]:
    """
    Updates an existing user's details.

    Args:
    user_id (int): The ID of the user to update.
    name (Optional[str]): New name of the user.
    email (Optional[str]): New email of the user.
    age (Optional[int]): New age of the user.

    Returns:
    Optional[User]: The updated User object if found, otherwise None.
    """
    with session_scope() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user is None:
            return None

        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if age is not None:
            user.age = age

        try:
            session.flush()
            session.refresh(user)
        except Exception as e:
            raise e

        return user


def delete_user(user_id: int) -> bool:
    """
    Deletes a user by ID.

    Args:
    user_id (int): The ID of the user to delete.

    Returns:
    bool: True if the user was deleted, False if the user was not found.
    """
    with session_scope() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user is None:
            return False

        session.delete(user)

        try:
            session.flush()
        except Exception as e:
            raise e

        return True
