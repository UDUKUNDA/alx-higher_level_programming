#!/usr/bin/python3
"""This one will fetch from a url that is specified below"""

import urllib.request

myUrl = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(myUrl) as response:

    bdy = response.read()
    bdy_str = bdy.decode('utf-8')

print("Body response:")
print("\t- type: {}".format(type(bdy)))
print("\t- content: {}".format(bdy))
print("\t- utf-8 content: {}".format(bdy_str))

