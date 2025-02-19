#!/usr/bin/python3
"""
free from injection
"""
import sys
import MySQLdb
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    query = """
    SELECT * FROM states WHERE name = %s ORDER BY id ASC
    """
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
