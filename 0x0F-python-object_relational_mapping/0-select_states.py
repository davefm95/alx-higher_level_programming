#!/usr/bin/python3
"""Shows all data in states table"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    """ List ststes in table """
    name, pwd, db_name = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(port=3306, user=name, password=pw, database=db_name)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    rows = c.fetchall()
    for row in rows:
        print(row)
