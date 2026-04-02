# Simple public API call for requests 

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_todos():
    try:
        response = requests.get(BASE_URL+"/todos", timeout=10)
    except requests.RequestException as e:
        print(f"Error fetching todos: {e}")
        return []

    response.raise_for_status()

    return response.json()


def fetch_users():
    # Makes the HTTP request (with a timeout at 10 s to avoid hanging forever)
    try:
        response = requests.get(BASE_URL+"/users", timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching users: {e}")
        return []

    # This will throw an error if the code is not 200 
    
    # Converts the json into python data
    return response.json()

def fetch_active_users():
    active_users = {"active_users" : []}

    todos = fetch_todos()
    users = fetch_users()

    print("Todos: ", todos[0])
    print("Users: ", users[0])

    userid_to_completed = {}
    
    # Map the number of todos to the user IDs that did them 
    for todo in todos:
        todo_user_id = todo.get("userId")
        completed_todo = todo.get("completed")

        if todo_user_id is not None and completed_todo is not None and completed_todo == True:
            if todo_user_id not in userid_to_completed:
                userid_to_completed[todo_user_id] = 1
            else:
                userid_to_completed[todo_user_id] += 1

    print(userid_to_completed)

    # Map users to user-ids
    user_id_to_user = {}
    for user in users:
        user_id = user.get("id")
        user_name = user.get("name")

        if user_id is not None and user_name is not None:
            if user_id not in user_id_to_user:
                user_id_to_user[user_id] = user_name
    
    print(user_id_to_user)

    # Go through the map of user_id to completed and add the ones that are active users

    for user_id, completed in userid_to_completed.items():
        if completed >= 5:
            # finds the user name
            name = user_id_to_user[user_id]
            active_user = {"userId" : user_id, "name" : name, "completedTodos" : completed}
            active_users["active_users"].append(active_user)

    print(active_users)
    return active_users

if __name__ == "__main__":
    print(fetch_active_users())