#!/usr/bin/python3
"""But this time, write one that is safe from MySQL injections!"""
import MySQLdb
import sys
if __name__ == '__main__':
    try:
        db = MySQLdb.connect(host='localhost',
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], port=3306)

        cur = db.cursor()

        cur.execute("SELECT cities.id as id, cities.name as name,\
        states.name FROM cities LEFT JOIN states ON\
        cities.state_id = states.id ORDER BY id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error(not Warning) as e:
        print(e)
