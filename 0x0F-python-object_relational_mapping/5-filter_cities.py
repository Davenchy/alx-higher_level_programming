#!/usr/bin/python3
"""Prints all States from the database"""

import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv[1:5]
    conn = MySQLdb.connect(
        user=args[0], passwd=args[1], db=args[2], port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT id, name
                FROM cities
                WHERE state_id =
                (
                    SELECT id
                    FROM states
                    WHERE name = %s
                    LIMIT 1
                )
                ORDER BY id ASC""", [args[3]])

    print(", ".join(map(lambda row: row[1], cur.fetchall())))
    cur.close()
    conn.close()
