#!/usr/bin/python3
"""
    Take a URL and an email, send a POST request and show response
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
