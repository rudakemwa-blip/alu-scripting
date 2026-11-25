#!/usr/bin/python3
"""Recursively retrieve all hot post titles from Reddit."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles using pagination."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu-reddit-api:v1.0 (by /u/redditor)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params={"limit": 100, "after": after},
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            return None if not hot_list else hot_list

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            return hot_list if hot_list else None

        for post in posts:
            title = post.get("data", {}).get("title")
            if title is not None:
                hot_list.append(title)

        next_after = data.get("after")
        if next_after is None:
            return hot_list

        return recurse(subreddit, hot_list, next_after)

    except (requests.RequestException, ValueError):
        return None if not hot_list else hot_list
