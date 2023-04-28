#!/usr/bin/python3
"""Senda post request to a ur with an email param"""
import sys
from urllib import request, parse
if __name__ == "__main__":
    prop = {'email': sys.argv[2]}
    data = parse.urlencode(prop).encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
