#!/usr/bin/python3
"""Prints all States where they name matches argument from the database"""

import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv[1:5]
    conn = MySQLdb.connect(user=args[0], passwd=args[1], db=args[2], port=3306)
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM states WHERE name LIKE '{args[3]}' ORDER BY id ASC")
    for state in cur.fetchall():
        print(state)

    cur.close()
    conn.close()
