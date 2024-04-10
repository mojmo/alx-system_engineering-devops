#!/usr/bin/python3

"""Fetch hot article titles from a given subreddit on Reddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to fetch hot article
    titles from a specified subreddit.

    Args:
    - subreddit (str): The name of the subreddit to query.
    - hot_list (list, optional): A list to store the hot article
    titles (default is an empty list).
    - after (str, optional): A token to paginate through the Reddit
    API results (default is None).

    Returns:
    - list: A list containing the titles of the hot articles from
    the specified subreddit.
    - None if there is an error retrieving the data or if the
    subreddit does not exist.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'custom_user_agent'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(
                                url,
                                headers=headers,
                                params=params,
                                allow_redirects=False
                            )

        if response.status_code == 200:
            data = response.json().get('data', {})
            after = data.get('after')
            articles = data.get('children', [])

            for article in articles:
                hot_list.append(article.get('data', {}).get('title'))

            if after is not None:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None
