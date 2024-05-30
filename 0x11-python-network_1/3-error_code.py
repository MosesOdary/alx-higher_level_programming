#!/usr/bin/python3
"""
    send a request to a URL and display the response
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
