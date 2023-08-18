#!/usr/bin/python3
"""Prints all States from the database"""

import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv[1:4]
    conn = MySQLdb.connect(
        user=args[0], passwd=args[1], db=args[2], port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT c.id, c.name, s.name
                FROM cities AS c
                JOIN states AS s
                ON c.state_id = s.id
                ORDER BY id ASC""")
    for state in cur.fetchall():
        print(state)

    cur.close()
    conn.close()
