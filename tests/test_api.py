from starlette.testclient import TestClient

from sqlalchemy.orm import Session


def test_health_check(db: Session, client: TestClient):
    """
    Test that the health check endpoint returns a 200 status code and expected JSON response.
    """
    # Make a GET request to the /api/healthcheck endpoint
    response = client.get("/api/healthcheck")

    # Check that the response status code is 200 OK
    assert response.status_code == 200

    # Verify the response content
    assert response.json() == {"status": "API is running"}


def test_create_user_success(db: Session, client: TestClient):
    """
    Test that a new user is created successfully when valid data is provided.
    """
    response = client.post(
        "/api/users/create",
        json={
            "name": "Jane Doe",
            "email": "janedoe@example.com",
            "age": 28
        }
    )

    # Check that the response status is 201 Created
    assert response.status_code == 201

    # Check that the response data matches the input data
    response_data = response.json()
    assert response_data["name"] == "Jane Doe"
    assert response_data["email"] == "janedoe@example.com"
    assert response_data["age"] == 28
