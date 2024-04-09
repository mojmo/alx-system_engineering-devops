#!/usr/bin/python3

"""retrieve the number of subscribers for a given subreddit on Reddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit on Reddit.

    Args:
    - subreddit (str): The name of the subreddit for which to retrieve
    the subscriber count.

    Returns:
    - int: The number of subscribers for the specified subreddit.
    - 0 if the subreddit does not exist or if there is an error
    retrieving the data.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:reddit_subscribers:v1.0 (by /u/mojmo)"}

    # Fetch user data
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        subscribers = response.json().get("data").get("subscribers")
        return subscribers

    return 0
