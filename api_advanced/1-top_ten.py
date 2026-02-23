#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the 10 hottest posts on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    results = response.json().get("data", {}).get("children", [])
    for post in results:
        print(post.get("data", {}).get("title"))
