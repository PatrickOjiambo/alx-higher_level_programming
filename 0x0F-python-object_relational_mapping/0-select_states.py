#!/usr/bin/python3
"""This file retrieves all the states from the database"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute('SELECT id, name FROM states ORDER BY id')
    rows = cur.fetchall()
    for (id_, name) in rows:
        print(f"({id_}, {name})")
    cur.close()
    db.close()
