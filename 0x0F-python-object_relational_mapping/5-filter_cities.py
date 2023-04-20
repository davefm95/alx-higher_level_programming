#!/usr/bin/python3
"""Lists all items of cities table"""

import MySQLdb as sql
from sys import argv
if __name__ == "__main__":
    user, pw, dn, stat = argv[1], argv[2], argv[3], argv[4]
    db = sql.connect(port=3306, user=user, password=pw, database=dn)
    c = db.cursor()
    query = """SELECT cities.name FROM cities
 JOIN states
 ON cities.state_id = states.id WHERE states.name = '{}'
 ORDER BY cities.id ASC"""
    c.execute(query.format(stat))
    rows = c.fetchall()
    isfirst = 1
    for row in rows:
        if isfirst:
            print(row[0], end='')
            isfirst = 0
            continue
        print(", {}".format(row[0]), end='')
    print()
