#!/usr/bin/python3
""" Response header value"""
from requests import get
from sys import argv


if __name__ == "__main__":
    response = get(argv[1])
    header_id = requests.headers.get('X-Request-Id')
    print(header_id)
