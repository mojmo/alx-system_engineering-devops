#!/usr/bin/python3

"""
This script fetches user and todo list data from the JSONPlaceholder API
based on the provided user ID. It then prints the user's name, the number of
completed tasks along with their titles, and exports the data to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    # Fetch user data
    user_response = requests.get(f"{url}users/{user_id}")
    user = user_response.json()

    # Fetch todos for the user
    todos_response = requests.get(f"{url}todos", params={"userId": user_id})
    todos = todos_response.json()

    # Prepare JSON data
    json_data = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in todos
        ]
    }

    # Write JSON data to file
    json_filename = f"{user_id}.json"

    with open(json_filename, "w") as file:
        json.dump(json_data, file)
