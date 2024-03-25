#!/usr/bin/python3

"""
This script fetches user and todo list data from the JSONPlaceholder API
based on the provided user ID. It then prints the user's name, the number
of completed tasks along with their titles, and exports the data to a CSV file.
"""

import csv
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

    # Extract completed tasks titles
    completed_tasks = [t.get("title") for t in todos if t.get("completed")]

    # Extract completed tasks and prepare CSV data
    tasks_data = []

    for task in todos:
        tasks_data.append([
            (user_id),
            user.get("name"),
            task.get("completed"),
            task.get("title")
        ])

    # Write CSV data to file
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks_data)
