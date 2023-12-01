#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""

import urllib.request
import sys


arguments = sys.argv
url = arguments[1]

with urllib.request.urlopen(url) as response:
    print(response.headers["X-Request-Id"])
