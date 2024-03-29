#!/usr/bin/python3
"""This file retrieves states that start with N"""
import MySQLdb
import sys
if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host='localhost',
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], port=3306)
        cur = db.cursor()
        cur.execute(
            'SELECT id, name FROM states WHERE name LIKE "N%" ORDER BY id ASC')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error(not Warning) as e:
        print(e)
