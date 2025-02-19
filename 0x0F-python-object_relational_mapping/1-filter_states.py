#!/usr/bin/python3
"""
lists states starting with N from hbtn_0c_0_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    state_list = """
    SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;
    """
    cursor.execute(state_list)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
