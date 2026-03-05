#!/usr/bin/python3
"""Module that recursively queries the Reddit API for all hot articles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
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
            hot_list.append(post.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list
    else:
        return None
