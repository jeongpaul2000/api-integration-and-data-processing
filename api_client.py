# Simple public API call for requests 

import requests

TEST_URL = "http://localhost:5000/hello_world"

def fetch_users():
    try:
        response = requests.get(TEST_URL, timeout=10)
        response.raise_for_status()
        
    except requests.RequestException as e:
        print(f"Error fetching users: {e}")
        return []

    return response


if __name__ == "__main__":
    response = fetch_users()

    # In Code Test Network

    assert 1 == 1
    print("Pass 1 == 1")
    assert response.status_code == 200
    print("Pass Status Code 200")
    assert response.json() == {"hello": "world"}
    print("Pass Data Contains Hello World")

    data = response.json()
    print(data)