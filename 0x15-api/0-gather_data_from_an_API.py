#!/usr/bin/python3

"""
This script fetches user and todo list data from the JSONPlaceholder API
based on the provided user ID. It then prints the user's name and the number
of completed tasks along with their titles.
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]

    # Fetch user data
    user_response = requests.get(f"{url}users/{user_id}")
    user = user_response.json()

    # Fetch todos for the user
    todos_response = requests.get(f"{url}todos", params={"userId": user_id})
    todos = todos_response.json()

    # Extract completed tasks titles
    completed_tasks = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"),
        len(completed_tasks),
        len(todos)
    ))

    for task in completed_tasks:
        print(f"\t {task}")
