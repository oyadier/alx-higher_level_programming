#!/usr/bin/python3
# Sent email using Post
"""
Post method practical
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


url = argv[1]
email = {'email': argv[2]}
email = urlencode(email)
email = email.encode('ascii')
request = Request(url, email)
with urlopen(request) as response:
string = response.read().decode('utf-8')
print(string)
