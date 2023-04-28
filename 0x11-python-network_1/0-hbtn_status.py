#!/usr/bin/python3
"""Yhis module visits a url and prints some info about it"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
    bytecontent = r.read()
    contentstring = bytecontent.decode('utf-8')
    ctype = type(bytecontent)
    print(f"""Body response:
    - type: {ctype}
    - content: {bytecontent}
    - utf8 content: {contentstring}""")
