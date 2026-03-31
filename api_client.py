# Simple public API call for requests 

import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_users():
    # Makes the HTTP request (with a timeout at 10 s to avoid hanging forever)
    response = requests.get(USERS_URL, timeout=10)

    # This will throw an error if the code is not 200 
    response.raise_for_status()

    # Converts the json into python data
    return response.json()

def get_user_summaries():
    users = fetch_users()

    summaries = []
    for user in users:
        summaries.append({
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"],
        })

    return summaries

if __name__ == "__main__":
    print(get_user_summaries())