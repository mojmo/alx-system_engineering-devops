#!/usr/bin/python3

"""
This script fetches user and todo list data from the JSONPlaceholder API for
all users. It then exports the data to a JSON file in the specified format.
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users_response = requests.get(f"{url}users")
    users = users_response.json()

    # Prepare JSON data
    all_data = {}

    for user in users:

        user_id = user.get("id")

        # Fetch todos for the user
        todos_response = requests.get(
                            f"{url}todos",
                            params={"userId": user_id}
                        )
        todos = todos_response.json()

        # Populate JSON data for this user
        user_data = [
            {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            } for task in todos
        ]

        all_data[user_id] = user_data

    # Write JSON data to file
    json_filename = "todo_all_employees.json"

    with open(json_filename, "w") as file:
        json.dump(all_data, file)
