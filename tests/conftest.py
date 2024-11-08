from typing import Generator
from unittest.mock import patch

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.db_control.session import Base

# SQLite database URL for testing
TEST_SQLALCHEMY_DATABASE_URL: str = "sqlite:///:memory:"
admin_engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL, isolation_level="AUTOCOMMIT"
)

# Create an engine and sessionmaker bound to the test database
engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)
TestingScopedSession = scoped_session(TestingSessionLocal)


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """
    This fixture creates the database with a “Session” scope. It sets up the tables before all tests
    and removes them after all tests are completed.
    """
    Base.metadata.create_all(bind=engine)  # Create tables
    yield
    Base.metadata.drop_all(bind=engine)  # Drop tables after tests


@pytest.fixture(scope="function")
def db() -> Generator:
    """
    Create a new database session for each test and roll it back after the test.
    """

    # Patch `Session` to use `TestingSessionLocal` instead of the original `Session`
    with patch("app.db_control.session.Session", new=TestingScopedSession):
        yield TestingScopedSession()

        # Rollback transaction
        TestingScopedSession.rollback()

        # Ensure the session is cleared after the test
        TestingScopedSession.remove()

