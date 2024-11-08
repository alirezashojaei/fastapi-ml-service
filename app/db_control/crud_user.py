import copy

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

    return user_object
