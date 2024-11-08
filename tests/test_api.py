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


def test_create_user_email_not_valid(db: Session, client: TestClient):
    """
    Test that an invalid email address is rejected when creating a new user.
    """
    response = client.post(
        "/api/users/create",
        json={
            "name": "Jane Doe",
            "email": "janedoe",  # Invalid email format
            "age": 28
        }
    )

    # Check that the response status is 422 Unprocessable Entity
    assert response.status_code == 422


def test_get_user_by_id_success(db: Session, client: TestClient):
    """
    Test that a user can be retrieved by ID.
    """
    # First, create a user to retrieve
    create_response = client.post(
        "/api/users/create",
        json={"name": "John Doe", "email": "johndoe@example.com", "age": 30}
    )
    user_id = create_response.json()["id"]

    # Now, retrieve the user by ID
    response = client.get(f"/api/users/{user_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == user_id
    assert response_data["name"] == "John Doe"
    assert response_data["email"] == "johndoe@example.com"
    assert response_data["age"] == 30


def test_get_user_by_id_not_found(db: Session, client: TestClient):
    """
    Test that retrieving a user that does not exist returns a 404 status code.
    """
    response = client.get("/api/users/99999")  # Assume this ID doesn't exist
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_update_user_success(db: Session, client: TestClient):
    """
    Test that an existing user's details can be updated successfully.
    """
    # First, create a user to update
    create_response = client.post(
        "/api/users/create",
        json={"name": "Jane Smith", "email": "janesmith@example.com", "age": 25}
    )
    user_id = create_response.json()["id"]

    # Update the user's details
    response = client.put(
        f"/api/users/{user_id}",
        json={"name": "Jane Updated", "email": "janeupdated@example.com", "age": 26}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == user_id
    assert response_data["name"] == "Jane Updated"
    assert response_data["email"] == "janeupdated@example.com"
    assert response_data["age"] == 26


def test_update_user_not_found(db: Session, client: TestClient):
    """
    Test that updating a user that does not exist returns a 404 status code.
    """
    response = client.put(
        "/api/users/99999",  # Assume this ID doesn't exist
        json={"name": "Nonexistent User", "email": "nonexistent@example.com", "age": 40}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_delete_user_success(db: Session, client: TestClient):
    """
    Test that a user can be deleted successfully.
    """
    # First, create a user to delete
    create_response = client.post(
        "/api/users/create",
        json={"name": "Delete Me", "email": "deleteme@example.com", "age": 29}
    )
    user_id = create_response.json()["id"]

    # Delete the user
    response = client.delete(f"/api/users/{user_id}")
    assert response.status_code == 204  # No content returned for delete

    # Verify the user no longer exists
    get_response = client.get(f"/api/users/{user_id}")
    assert get_response.status_code == 404


def test_delete_user_not_found(db: Session, client: TestClient):
    """
    Test that deleting a user that does not exist returns a 404 status code.
    """
    response = client.delete("/api/users/99999")  # Assume this ID doesn't exist
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
