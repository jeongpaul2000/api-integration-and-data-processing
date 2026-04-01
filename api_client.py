# Simple public API call for requests 

import requests

USERS_URL = "http://localhost:5000/hello_world"

def fetch_users():
    # Makes the HTTP request (with a timeout at 10 s to avoid hanging forever)
    try:
        response = requests.get(USERS_URL, timeout=10)
    except requests.RequestException as e:
        print(f"Error fetching users: {e}")
        return []

    # This will throw an error if the code is not 200 
    response.raise_for_status()

    # Converts the json into python data
    return response


if __name__ == "__main__":
    response = fetch_users()
    assert 1 == 1
    print("Pass 1 == 1")
    assert response.status_code == 200
    print("Pass Status Code 200")
    assert response.json() == {"hello": "world"}
    print("Pass Data Contains Hello World")
    data = response.json()
    print(data)