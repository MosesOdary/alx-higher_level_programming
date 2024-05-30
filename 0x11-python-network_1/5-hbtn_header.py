#!/usr/bin/python3
"""
    Take a URL, send a request and display X-Request-Id
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
