import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test the /activities endpoint
def test_get_activities():
    # Arrange
    expected_keys = ["Chess Club", "Programming Class", "Gym Class"]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    for key in expected_keys:
        assert key in data

# Test the /activities/{activity_name}/signup endpoint
def test_signup_for_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "new_student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}

# Test the /activities/{activity_name}/unregister endpoint
def test_unregister_from_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "new_student@mergington.edu"
    signup_response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert signup_response.status_code == 200

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}