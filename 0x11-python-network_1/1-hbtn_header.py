#!/usr/bin/python3
"""displays the avlue of the requset if of a http request"""
import sys
import urllib.request
with urllib.request.urlopen(sys.argv[1]) as resp:
    print(resp.info()['X-Request-Id'])
