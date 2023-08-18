#!/usr/bin/python3
"""Prints all States starting with N from the database"""

import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv[1:4]
    conn = MySQLdb.connect(user=args[0], passwd=args[1], db=args[2], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for state in cur.fetchall():
        print(state)

    cur.close()
    conn.close()
