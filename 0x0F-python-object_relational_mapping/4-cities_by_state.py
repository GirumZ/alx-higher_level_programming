#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb


if __name__ == '__main__':

    args = sys.argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities JOIN states ON cities.state_id = states.id;")
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
