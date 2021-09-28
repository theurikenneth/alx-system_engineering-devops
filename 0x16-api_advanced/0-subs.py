#!/usr/bin/pyhton3
""" returns the number of subscribers """
import requests

url = "https://www.reddit.com/r/{}/about.json"


def number_of_subscribers(subreddit):
    """ gets the number of subscribers """
    header = {'user-agent': 'holberton'}
    r = requests.get(url.format(subreddit), headers=header)
    if r.status_code != 200:
        return 0
    return r.json().get("data", {}).get("subscribers", 0)
