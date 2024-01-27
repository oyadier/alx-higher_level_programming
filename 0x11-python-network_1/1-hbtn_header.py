#!/usr/bin/python3
# Get the id of a request
"""Get the request id from the url content"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        content = resp.read()
        response_id = resp.headers.get('X-Request-Id')
        print(response_id)
