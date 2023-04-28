#!/usr/bin/python3
"""This sends an email fayat toba url"""
import sys
import requests
if __name__ == "__main__":
    info = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=info)
    print(r.text)
