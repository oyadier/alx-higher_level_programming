#!/usr/bin/python3
"""Fetch resourse with urllib moduel"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    content = res.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
