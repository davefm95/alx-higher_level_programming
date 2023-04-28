#!/usr/bin/python3
"""This module uses requests package to get and print a url resourxe"""
import requests
if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    txtype = type(r.text)
    print("""Body response:
    - type: {}
    - content: {}""".format(txtype, r.text))
