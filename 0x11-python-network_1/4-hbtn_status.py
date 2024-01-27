#!/usr/bin/python3
"""Fetch url using only request package"""
import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status',
                            auth=('user', 'pass'))
    print("Body response")
    print(f"\t- type: {str(response)}")
    print(f"\t- content: {response.text}")
