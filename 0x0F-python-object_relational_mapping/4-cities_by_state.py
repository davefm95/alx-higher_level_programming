#!/usr/bin/python3
"""Lists all items of cities table"""

import MySQLdb as sql
from sys import argv
if __name__ == "__main__":
    user, pw, dn = argv[1], argv[2], argv[3]
    db = sql.connect(port=3306, user=user, password=pw, database=dn)
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
