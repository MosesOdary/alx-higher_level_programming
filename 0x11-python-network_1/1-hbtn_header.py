#!/usr/bin/python3
"""
    Take a URL, send a request to URL and display X-Request-Id
"""
import sys

import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
