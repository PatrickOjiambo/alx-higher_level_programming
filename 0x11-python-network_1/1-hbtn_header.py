#!/usr/bin/python3
"""Get the xRequestid"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        body = response.info()
        xRequestId = body.get('X-Request-Id')
        if xRequestId:
            print(xRequestId)
