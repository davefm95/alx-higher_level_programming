#!/usr/bin/python3
"""Tbis tajes a url amd displays the body"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError
req = Request(argv[1])
try:
    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
except HTTPError as e:
    print(f"Error code: {e.code}")
