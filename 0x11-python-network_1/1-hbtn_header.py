#!/usr/bin/python3
"""displays the avlue of the requset if of a http request"""
from sys import argv
import urllib.request
with urllib.request.urlopen(argv[1]) as resp:
    print(resp.info()['X-Request-Id'])
