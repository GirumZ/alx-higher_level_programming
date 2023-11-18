#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == '__main__':

    args = sys.argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    query = ("SELECT cities.name FROM cities INNER JOIN states "
             "ON cities.state_id = states.id AND states.name = %s "
             "ORDER BY cities.id")
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))

    cur.close()
    conn.close()
