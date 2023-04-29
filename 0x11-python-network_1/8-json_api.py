#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user"""
import sys
import requests
if __name__ == "__main__":
    info = {'q': ""}
    if sys.argv[1]:
        info['q'] = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data=info)
    try:
        r.json()
        if r.content > 0:
            idee = r.json()['id']
            nm = r.json()['name']
            print(f"[{idee}] {nm}")
        else:
            print("No result")
    except ValueError:
        print(" Not a valid JSON")
