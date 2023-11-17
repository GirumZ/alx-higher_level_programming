#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb


def main():
    """ Interacts with a database"""


args = sys.argv

conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                       passwd=args[2], db=args[3], charset="utf8")
cur = conn.cursor()
query = "SELECT * FROM states ORDER BY id ASC"
cur.execute(query)
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()

if __name__ == '__main__':
    main()
