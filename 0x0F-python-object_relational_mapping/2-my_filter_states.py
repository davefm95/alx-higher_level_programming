#!/usr/bin/python3
"""This module returns a record with a name match"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
