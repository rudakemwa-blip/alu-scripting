#!/usr/bin/python3
"""Print the first ten hot posts from a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first ten hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu-reddit-api:v1.0 (by /u/redditor)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 10},
            allow_redirects=False,
            timeout=10
        )
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    except (requests.RequestException, ValueError):
        print(None)
