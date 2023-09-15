#!/usr/bin/python3
"""This file displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys
if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host='localhost',
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], port=3306)
        state_searched = sys.argv[4]
        cur = db.cursor()

        cur.execute(
            'SELECT id, name FROM states WHERE name = "{}"'
            .format(state_searched))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error(not Warning) as e:
        print(e)
