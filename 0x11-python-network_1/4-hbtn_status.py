#!/usr/bin/python3
"""Fetch url using only request package"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status',
                            auth=('user', 'pass'))
    str_type = response.text
    print("Body response")
    print(f"\t- type: {type(str_type)}")
    print(f"\t- content: {str_type}")
