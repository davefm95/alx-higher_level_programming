#!/usr/bin/python3
"""displays the avlue of the requset if of a http """
import sys
import urllib.request
with urllib.request.urlopen(sys.argv[1]) as resp:
    print(resp.info().get('X-Request-Id'))
