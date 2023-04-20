#!/usr/bin/python3
"""Shows all data in states table that matchrs given param"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    """ List ststes in table """
    name, pw, db_name, search = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(port=3306, user=name, password=pw, database=db_name)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = '{}'".format(search))
    rows = c.fetchall()
    for row in rows:
        print(row)
