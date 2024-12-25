#!/usr/bin/python3
"""
where name matches argument 4
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched_state = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
            (searched_state,)
            )
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
