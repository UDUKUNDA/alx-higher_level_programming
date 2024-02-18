#!/usr/bin/python3
"""
This takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """
    This takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
    """
    url = argv[1]
    requst = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(requst) as response:
            bdy = response.read()
            bdy_str = bdy.decode('utf-8')
            print(bdy_str)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
