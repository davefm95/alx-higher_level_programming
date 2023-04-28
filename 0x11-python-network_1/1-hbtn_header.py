#!/usr/bin/python3
"""displays the avlue of the requset if of a http request"""
from sys import argv
import urllib.request
req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as resp:
    print(resp.info()['X-Request-Id'])
