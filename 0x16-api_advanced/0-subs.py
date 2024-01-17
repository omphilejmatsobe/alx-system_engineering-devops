#!/usr/bin/python3
"""
    Module for number of subscribers
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    res = requests.get(url, headers=headers,
                       allow_redirects=False)
    if str(res) != "<Response [200]>":
        return 0
    data = res.json()
    num = data.get("data").get("subscribers")
    return num
