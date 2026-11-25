#!/usr/bin/python3
"""Count keyword occurrences in hot Reddit post titles."""

import re

from requests import RequestException

from requests import get


def count_words(subreddit, word_list):
    """Recursively count and print matching words in hot post titles."""
    counts = {}
    keywords = [word.lower() for word in word_list]

    def fetch(after=None):
        """Recursively fetch Reddit hot posts."""
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {
            "User-Agent": "python:alu-reddit-api:v1.0 (by /u/redditor)"
        }

        try:
            response = get(
                url,
                headers=headers,
                params={"limit": 100, "after": after},
                allow_redirects=False,
                timeout=10
            )

            if response.status_code != 200:
                return False

            data = response.json().get("data", {})
            posts = data.get("children", [])

            for post in posts:
                title = post.get("data", {}).get("title", "").lower()
                words = re.findall(r"\b[a-z0-9]+\b", title)

                for keyword in keywords:
                    counts[keyword] = counts.get(keyword, 0) + words.count(
                        keyword
                    )

            next_after = data.get("after")
            if next_after is not None:
                return fetch(next_after)

            return True

        except (RequestException, ValueError):
            return False

    if not fetch():
        return

    results = [
        (word, count)
        for word, count in counts.items()
        if count > 0
    ]

    for word, count in sorted(results, key=lambda item: (-item[1], item[0])):
        print("{}: {}".format(word, count))


if __name__ == "__main__":
    pass
