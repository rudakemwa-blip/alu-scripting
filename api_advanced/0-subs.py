#!/usr/bin/python3
"""Query the Reddit API for subreddit subscriber counts."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu-reddit-api:v1.0 (by /u/redditor)"
    }

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError):
        return 0
