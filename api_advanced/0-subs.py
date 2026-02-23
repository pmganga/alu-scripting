#!/usr/bin/python3
"""
Module that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers.
    If the subreddit is invalid, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Strictly formatted API User-Agent to comply with Reddit's rules
    headers = {"User-Agent": "python:alu.api.advanced:v1.0 (by /u/philip)"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0
        
    data = response.json().get("data", {})
    return data.get("subscribers", 0)
