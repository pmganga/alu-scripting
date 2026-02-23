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
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0"}

    # Notice we removed params={"limit": 10} so the mock server doesn't break
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    if not children:
        print("None")
        return

    # Slicing the array ensures we only ever print 10 titles
    for post in children[:10]:
        print(post.get("data", {}).get("title"))
