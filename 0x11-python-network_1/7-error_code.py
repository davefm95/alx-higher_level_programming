#!/usr/bin/python3
"""semds req to url amd displays body of respomse"""
import sys
import requests
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code > 399:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
    
