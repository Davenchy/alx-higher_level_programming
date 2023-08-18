#!/usr/bin/python3
"""Prints all States from the database"""


def main():
    """The main function of the program"""

    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    [username, password, database] = sys.argv[1:4]

    db = MySQLdb.connect(host="127.0.0.1", port=3306,
                         user=username, passwd=password, db=database,
                         charset="utf8")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == "__main__":
    main()
