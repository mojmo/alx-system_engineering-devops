#!/usr/bin/python3

"""
retrieve and print the top 10 posts (by upvotes) for
a given subreddit on Reddit.
"""

import requests


def top_ten(subreddit):
    """
    Retrieve and print the top 10 posts (by upvotes) for
    a given subreddit on Reddit.

    Args:
    - subreddit (str): The name of the subreddit for which
    to retrieve the top posts.

    Prints:
    - The titles of the top 10 posts for the specified subreddit.
    - "None" if there are no posts or if there is an error retrieving the data.
    """

    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:reddit_subscribers:v1.0 (by /u/mojmo)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        children = response.json().get("data").get("children")

        for child in children:
            print(child.get("data").get("title"))
    else:
        print("None")
