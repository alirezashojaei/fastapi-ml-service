import os
from typing import Generator
from unittest.mock import patch

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from starlette.testclient import TestClient

from app.db_control.session import Base
from app.main import app

# SQLite database URL for testing
TEST_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../test.db")
TEST_SQLALCHEMY_DATABASE_URL = f"sqlite:///{TEST_DB_PATH}"

# Create an engine and sessionmaker bound to the test database
engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
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

    # Remove the test database file after the test session
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)


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
        TestingScopedSession.remove()


@pytest.fixture(scope="function")
def client(db: Session) -> Generator[TestClient, None, None]:
    """
    Provide a TestClient that uses the test database session.
    """
    with TestClient(app) as c:
        yield c
