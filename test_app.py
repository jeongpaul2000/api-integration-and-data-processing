# A bit more complicated test verifying JSON response shape and status codes from the API endpoint.

# Importing app elements from app.pty to test the API endpoint
from app import app

def test_hello_world():
    client = app.test_client()
    response = client.get("/hello_world")

    # Print Statements do not work in pytest environment unless explicitly run the actual test script in python
    assert response.status_code == 200
    assert response.get_json() == {"hello": "world"}
