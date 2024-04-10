#!/usr/bin/python3

"""
This script provides a recursive function to query the Reddit API,
parse the titles of hot articles from a specified subreddit,
and print a sorted count of given keywords. The function counts
occurrences of each keyword in the titles of the hot articles.
"""

import requests
import re


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API and prints a sorted count
    of given keywords.

    Args:
    - subreddit (str): The name of the subreddit to query.
    - word_list (list): A list of keywords to count occurrences of.
    - after (str, optional): A token to paginate through the Reddit
    API results (default is None).
    - word_count (dict, optional): A dictionary to store the counts
    of keywords (default is an empty dictionary).

    Returns:
    - None
    """

    headers = {'User-Agent': 'custom_user_agent'}
    params = {'after': after} if after else {}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    # Initialize word counts if after is None (first call of the function)
    if after is None:
        for word in word_list:
            word_lower = word.lower()
            if word_lower not in word_count:
                word_count[word_lower] = 0

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

        # Iterate through articles and count occurrences of
        # each keyword in titles
        for article in articles:
            title = article.get('data', {}).get('title', '').lower()
            for word in word_list:
                word_lower = word.lower()
                word_count[word_lower] += len(re.findall(r'\b{}\b'.format(
                    re.escape(word_lower)), title))

        # If there are more articles, recursively call the
        # function with the 'after' token
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(
                                word_count.items(),
                                key=lambda kv: (-kv[1], kv[0])
                            )
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")
            return
    else:
        return
