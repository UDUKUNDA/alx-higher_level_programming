#!/usr/bin/python3
"""
This lists 10 commits (from the most recent to oldest) of the repository “rails”
by the user “rails”
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    This lists 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”
    """
    myRepo = argv[1]
    theOwner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(theOwner, myRepo)
    r = requests.get(url)
    res_list = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(res_list[i].get('sha'), res_list[i].
                                  get('commit').get('author').get('name')))
    except:
        pass
