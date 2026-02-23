#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the 10 hottest posts on a given subreddit.
    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alu.api.advanced:v1.0 (by /u/philip)"}
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        print("None")
        return

    # Slicing [0:10] ensures we strictly print 10,
    # even if Reddit returns stickied posts
    for post in posts[0:10]:
        print(post.get("data", {}).get("title"))
