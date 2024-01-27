#!/usr/bin/python3
"""Send email using Post"""
from sys import argv
import requests


if __name__ == "__main__":
    email = {'email': argv[2]}
    url = argv[1]
    response = requests.post(url, email=email)
    print(response)

