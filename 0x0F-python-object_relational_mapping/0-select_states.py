#!/usr/bin/python3
"""Prints all States from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    [username, password, database] = sys.argv[1:4]

    conn = MySQLdb.connect(host="127.0.0.1", port=3306,
                           user=username, passwd=password, db=database,
                           charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
