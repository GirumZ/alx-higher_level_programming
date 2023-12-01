#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":

    data = {"q", ""}
    if len(sys.argv) > 1:
        data["q"] = sys.argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", data)
    if "json" not in req.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        if req.json():
            print("[{}] {}".format(req.json().get()('id'), req.json.get('name')))
        else:
            print("No result")
