#!/usr/bin/python3
"""This module adds arguments to a list and saves to a file"""
import os
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


f = "add_item.json"
if not os.path.exists(f) or os.path.getsize(f) == 0:
    lst = []
    if len(argv) > 1:
        lst += argv[1:]
    save_to_json_file(lst, f)
else:
    lst = load_from_json_file(f)
    if len(argv) > 1:
        lst += argv[1:]
    save_to_json_file(lst, f)
