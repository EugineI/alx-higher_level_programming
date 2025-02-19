#!/usr/bin/python3
"""
this script lists all the states from the database hbtn_0c_0_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    state_list = """
    SELECT * FROM states ORDER BY id ASC;
    """
    cursor.execute(state_list)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
