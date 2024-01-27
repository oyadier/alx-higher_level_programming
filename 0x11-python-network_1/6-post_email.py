#!/usr/bin/python3
"""Send email using Post"""
from sys import argv
import requests


if __name__ == "__main__":
    send_email = {'email': argv[2]}
    url = argv[1]
    response = requests.post(url, data=send_email)
    print(response.text)
