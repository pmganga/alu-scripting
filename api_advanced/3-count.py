#!/usr/bin/python3
"""Module that recursively counts keywords in Reddit hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """Prints a sorted count of given keywords case-insensitively."""
    if word_counts is None:
        word_counts = {}
        for word in word_list:
            word = word.lower()
            if word not in word_counts:
                word_counts[word] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api.advanced:v1.0.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json().get("data", {})
        after = data.get("after")
        children = data.get("children", [])

        for post in children:
            title_words = post.get("data", {}).get("title").lower().split()
            for word in word_counts.keys():
                word_counts[word] += title_words.count(word)

        if after is not None:
            return count_words(subreddit, word_list, after, word_counts)
        else:
            sorted_counts = sorted(
                word_counts.items(), key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_counts:
                if count > 0:
                    print("{}: {}".format(word, count))
    else:
        return
