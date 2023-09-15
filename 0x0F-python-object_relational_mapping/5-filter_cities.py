#!/usr/bin/python3
"""But this time, write one that is safe from MySQL injections!"""
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
            'SELECT name FROM cities WHERE state_id = (SELECT id FROM\
            states WHERE name = %s)', (state_searched, ))
        rows = cur.fetchall()
        names = [row[0] for row in rows]
        result = ", ".join(names)
        print(result)
        cur.close()
        db.close()
    except MySQLdb.Error(not Warning) as e:
        print(e)
